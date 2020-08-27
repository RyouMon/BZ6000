from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers


@api_view(['GET', 'POST'])
def students(request, format=None):
    """
    list all students, or create a new student.
    """
    if request.method == 'GET':
        student_li = models.Student.objects.all()
        serializer = serializers.StudentSerializer(student_li, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk, format=None):
    """
    Retrieve, update or delete a student.
    """
    try:
        student = models.Student.objects.get(pk=pk)
    except models.Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def groups(request, format=None):
    """
    list all groups, or create a new group.
    """
    if request.method == 'GET':
        group_li = models.Group.objects.all()
        serializer = serializers.GroupSerializer(group_li, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def group_detail(request, pk, format=None):
    """
    Retrieve, update or delete a group.
    """
    try:
        group = models.Group.objects.get(pk=pk)
    except models.Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.GroupSerializer(group)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
