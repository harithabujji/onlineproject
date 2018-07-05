from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from onlineapp.models import *

class CollegeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=128)
    location = serializers.CharField(max_length=64)
    acronym = serializers.CharField(max_length=8)
    contact = serializers.EmailField()

    def create(self, validated_data):
        return College.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.acronym = validated_data.get('acronym', instance.acronym)
        instance.contact = validated_data.get('contact',instance.contact)
        instance.save()
        return instance

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name=serializers.CharField(max_length=128)
    #dob = serializers.DateField(null=True, blank=True)
    email =serializers.EmailField()
    db_folder = serializers.CharField(max_length=60)


    dropped_out = serializers.BooleanField(default=False)

    college_id=serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email',  instance.email )
        instance.db_folder = validated_data.get('db_folder', instance.db_folder)
        instance.dropped_out = validated_data.get('dropped_out',instance.dropped_out)
        instance.college_id = validated_data.get('college_id', instance.college_id)
        instance.save()
        return instance
#
# class StudentMarksSerializer(serializers.Serializer):
#     problem1 = serializers.IntegerField()
#     problem2 = serializers.IntegerField()
#     problem3 = serializers.IntegerField()
#     problem4 = serializers.IntegerField()
#     total = serializers.IntegerField()
#
#     student=StudentSerializer
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.problem1 = validated_data.get(' problem1', instance. problem1)
#         instance. problem2 = validated_data.get(' problem2',  instance. problem2 )
#         instance.problem3 = validated_data.get('problem3', instance.problem3)
#         instance.problem4 = validated_data.get('problem4',instance.problem4)
#         instance.total = validated_data.get('total', instance.total)
#         instance.student=validated_data.get('student', instance.student)
#         instance.save()
#         return instance
class MockTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockTest1
        fields = ('id','problem1','problem2','problem3','problem4','total','student')


class StudentDetailsSerializer(serializers.ModelSerializer):

    mocktest1=MockTestSerializer(required=True)
    class Meta:
        model=Student
        fields='__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.db_folder = validated_data.get('db_folder', instance.db_folder)
        instance.dropped_out = validated_data.get('dropped_out', instance.dropped_out)
        instance.college_id = validated_data.get('college_id', instance.college_id)
        instance.problem1 = validated_data.get(' problem1', instance.problem1)
        instance.problem2 = validated_data.get(' problem2', instance.problem2)
        instance.problem3 = validated_data.get('problem3', instance.problem3)
        instance.problem4 = validated_data.get('problem4', instance.problem4)
        instance.total = validated_data.get('total', instance.total)
        instance.student = validated_data.get('student', instance.student)
        instance.save()
        return instance




