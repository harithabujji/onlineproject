from django.urls import path
from . import views
from onlineapp.views import *

from onlineapp.restAPI import *

app_name="onlineapp"

urlpatterns=[
    #path('jki/',views.my_html_view),
    #path('clg/<int:s_id>/',views.student_data),
    #path('mrks/',views.student_marks),
    #path('clgo/<int:c_id>/',views.clg_order),
    #path('testsession/',views.test_session),
    #path('',views.helloworld),
    #path('exce/',views.check_exception),

    path('clgs/',CollegeView.as_view(),name="colleges"),

    path('colleges/',CollegeListView.as_view(),name="college_html"),

    path('colleges/add',CreateCollegeView.as_view(),name="add_colleges"),

    path('colleges/<int:pk>/edit', UpdateCollegeView.as_view(), name="edit_college"),

    path('colleges/<int:pk>/delete', DeleteCollegeView.as_view(), name="delete_college"),


    path('colleges1/<int:pk>/', CollegeDetailView.as_view(), name="college_detail_html"),

    path('colleges1/<int:pk>/add', CreateStudentView.as_view(), name="college_detail.html"),

    path('colleges/<int:college_id>/edit/<int:pk>/', UpdateStudentView.as_view(), name='edit_student'),

    path('colleges/<int:college_id>/<int:pk>/delete', DeleteStudentView.as_view(), name='delete_student'),


    path('signup/',SignupController.as_view(),name="signup"),

    path('login/',LoginController.as_view(),name="login"),

    path('logout/',logout_user,name="logout"),





    path('api/v2/clg/', clgg_list),
    path('clg_detail/<int:pk>/', snippet_detail),

    path('std/', student_list),
    path('std_detail/<int:pk>/', Student_detail),

    path('clgst/<int:pk>/', StudentsOfClgView.as_view()),

    path('clgstudents/clg/<int:clg_id>/stdnt/<int:pk>/',college_detail),

    path('studentsinclg/clg/<int:clg_id>/stdnt/<int:pk>/',StudentMarksView.as_view())



]
