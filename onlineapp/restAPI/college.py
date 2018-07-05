from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from onlineapp.serialize import *

@csrf_exempt
@api_view(['POST','GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def clgg_list(request):
    if request.method == 'GET':
        clg_list = College.objects.all()
        serializer = CollegeSerializer(clg_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = College.objects.get(pk=pk)
    except College.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CollegeSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = CollegeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class StudentsOfClgView(APIView):

    def get(self, request, pk, format=None):
        snippet = Student.objects.filter(college_id = pk)
        serializer = StudentSerializer(snippet,many=True)
        return JsonResponse(serializer.data,safe=False)

    def post(self,request, pk, format=None):
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




@csrf_exempt
@api_view(['GET','PUT','DELETE'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def college_detail(request,clg_id, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        college=Student.objects.filter(college_id=clg_id)
        snippet =Student.objects.filter(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentDetailsSerializer(snippet,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'PUT':
        serializer = StudentDetailsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

