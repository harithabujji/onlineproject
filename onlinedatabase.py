import os
import sys
import click
import openpyxl as xl
from bs4 import BeautifulSoup
import django
from django.db import models
import MySQLdb
from onlineproject import settings


#creates environment variable for running django commands through script.
def setup_django():
    os.environ["DJANGO_SETTINGS_MODULE"] = 'onlineproject.settings'
    django.setup()


#Deals with manage.py and migrations
def set_migrations():
    os.system("manage.py migrate")
    os.system("manage.py makemigrations")






#Returns the database object.
#creates the database object from onlineproject.settings.DATABASES dict.
def get_db_connection():
    db=MySQLdb.connect("localhost", "root", "haritha123", name=settings.DATABASES["default"]["NAME"])
    return db

#returns dbname from onlineproject.settings.DATABASES dict
def get_db_name():
    return settings.DATABASES["default"]["NAME"]

def close_db(db_obj):
    db_obj.close()




#Data populating functions.

#Populates college table.
def populate_college():

    #importing College.
    from onlineapp.models import College

    #Worksheets loading.
    wb_students = xl.load_workbook("students.xlsx")

    #Getting Colleges worksheet.
    clg_sheet = wb_students["Colleges"]

    #Dict for holding objects of Colleges.
    college_obj_dict={}

    #Populating data into College.
    for row in [x for x in clg_sheet][1:]:
        college_obj_dict[row[1].value.strip()]=College(name=row[0].value.strip(),location=row[2].value.strip(),
                                                       acronym=row[1].value.strip(),contact=row[3].value.strip())

        college_obj_dict[row[1].value.strip()].save()
    #returning college_obj_dict to populatedata.
    return college_obj_dict

    pass


#Populates students table.
def populate_students(college_objects):
    # importing Student
    from onlineapp.models import Student

    # Worksheets loading.
    wb_students = xl.load_workbook("students.xlsx")

    # Getting Current and deletes worksheets.
    current_sheet = wb_students["Current"]
    delete_sheet=wb_students["Deletions"]


    #Dict for holding objects of Students.
    student_obj_dict = {}

    #Populating data into Student from Current.
    for row in [x for x in current_sheet][1:]:
        student_obj_dict[row[3].value.lower().strip()] = Student(name=row[0].value.strip(), email=row[2].value.strip(),
                                                                 db_folder=row[3].value.strip(),
                                                                 college=college_objects[row[1].value.strip()])
        student_obj_dict[row[3].value.lower().strip()].save()

    # Populating data into Student from Deletes.
    for row in [x for x in delete_sheet][1:]:
        student_obj_dict[row[3].value.lower().strip()] = Student(name=row[0].value.strip(),email=row[2].value.strip(),
                                                                db_folder=row[3].value.strip(),
                                                                 college=college_objects[row[1].value.strip()],
                                                                 dropped_out=True)
        student_obj_dict[row[3].value.lower().strip()].save()


    # returning college_obj_dict to populatedata.
    return student_obj_dict

    pass


def populate_marks(students_objs):

    # importing MockTest
    from onlineapp.models import MockTest1

    #Getting data from html file.
    with open("mock_test.html") as fp:
        soup = BeautifulSoup(fp, "lxml")

    #Getting all rows and columns and inserting into MockTest table.
    trs = soup.find_all('tr')
    for i in range(1, len(trs)):
        thds = trs[i].find_all(['th', 'td'])
        try:
            obj=MockTest1(problem1=int(thds[2].text),problem2=int(thds[3].text),problem3=int(thds[4].text),
                     problem4=int(thds[5].text),total=int(thds[6].text),student=students_objs[thds[1].text.split('_')[2]])
            obj.save()
        except KeyError:
            pass
    pass



#group for commands in onlinedb.py
@click.group()
def onlinedb1():
    pass


# command for creating a db.
# It will get dbname from onlineproject.settings
@onlinedb1.command()
def createdb():
    db=get_db_connection()
    db_name=get_db_name()

    cur = db.cursor()
    #Creating database.
    cur.execute("create database {}".format(db_name))
    cur.close()

    close_db(db)
    pass


# command for dropping a db.
# It will get dbname specified in onlineproject.settings
@onlinedb1.command()
def dropdb():
    db = get_db_connection()
    db_name = get_db_name()
    cur = db.cursor()
    # Dropping database.
    cur.execute("drop database {}".format(db_name))
    close_db(db)
    pass




#command for populating data.
#It will get data from an excel sheet and html page.
#uses openpyxl and BeautifulSoup module.
@onlinedb1.command()
def populatedata():

    #
    setup_django()

    #setting migrations.
    set_migrations()


    #populating data into tables.

    #1.Populating data into college table.
    college_objects=populate_college()

    #2.Populating data into student table.
    student_objects=populate_students(college_objects)

    #3.Populating data into marks tables.
    populate_marks(student_objects)
    pass




#command for clear data in database.
@onlinedb1.command()
def cleardata():


    setup_django()
    from onlineapp.models import College, MockTest1, Student


    MockTest1.objects.all().delete()
    Student.objects.all().delete()
    College.objects.all().delete()
    pass



#main function.
if __name__=="__main__":
    onlinedb1()
    setup_django()


