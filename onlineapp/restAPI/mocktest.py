from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from onlineapp.serialize import *


@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def Student_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentDetailsSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentDetailsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


