##from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from salesmen.models import Task, Employee, Responsibility
from salesmen.serializers import TaskSerializer, EmployeeSerializer, ResponsibilitySerializer

class TaskList(APIView):

    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeList(APIView):

    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResponsibilityList(APIView):

    def get(self, request, format=None):
        responsibilities = Responsibility.objects.all()
        serializer = ResponsibilitySerializer(responsibilities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ResponsibilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)