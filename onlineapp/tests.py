from django.test import TestCase
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","onlineproject.settings")
django.setup()

# from onlineapp.models import *
# # Create your tests here.
# manager=College.objects
# querysets=College.objects.all()
# print(querysets)
# for qs in querysets:
#     print(qs)



from django.test import TestCase
from onlineapp.serialize import *
# Create your tests here.


class CollegeTestCase(TestCase):

    def setUp(self):
        self.colleges=College.objects.create(name="lion", location ="roar",acronym='cbj',contact='nk@gmail.com')
        self.college_serializer=CollegeSerializer(self.colleges)

    def test_college_valid_serialize(self):
        self.assertEqual(self.college_serializer.data, {'name': "lion", 'location': "roar", 'acronym': 'cbj', 'contact': 'nk@gmail.com'})

    def test_college_invalid_serialize(self):
        self.assertNotEqual(self.college_serializer.data,
                         {'name': "lion1", 'location': "roar", 'acronym': 'cbj', 'contact': 'nk@gmail.com'})


