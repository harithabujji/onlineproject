from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from onlineapp.serialize import *

@csrf_exempt
@api_view(['POST','GET'])
def student_list(request):
    if request.method == 'GET':
        stdnt_list = Student.objects.all()
        serializer = StudentSerializer(stdnt_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class StudentMarksView(APIView):

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, clg_id, pk, format=None):
        student = self.get_object(pk)
        mocky = MockTest1.objects.get(student_id=pk)
        student.mocky = mocky
        serializer = StudentDetailsSerializer(student)
        return JsonResponse(serializer.data)


    def put(self, request,clg_id, pk, format=None):
        student = self.get_object(pk)
        mocky = MockTest1.objects.get(student_id=pk)
        student.mocky = mocky
        serializer = StudentDetailsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self,request,clg_id, pk, format=None):
        snippet1 = Student.objects.filter(college_id=clg_id)
        snippet2 = Student.objects.filter(pk=pk)
        snippet2.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


class StudentsMarksEnterView(APIView):

    def get(self, request, pk, format=None):
        snippet = Student.objects.filter(college_id=pk)
        serializer = StudentSerializer(snippet, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self,request, pk, format=None):
        data = JSONParser().parse(request)
        college = College.objects.get(id = pk)
        serializer = StudentDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save(college = college)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)