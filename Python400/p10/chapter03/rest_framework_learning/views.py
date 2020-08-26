from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from . import models
from . import serializers


@csrf_exempt
def students(request):
    """
    list all students, or create a new student.
    """
    if request.method == 'GET':
        student_li = models.Student.objects.all()
        serializer = serializers.StudentSerializer(student_li, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def student_detail(request, pk):
    """
    Retrieve, update or delete a student.
    """
    try:
        student = models.Student.objects.get(pk=pk)
    except models.Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = serializers.StudentSerializer(student)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = serializers.StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=True)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)
