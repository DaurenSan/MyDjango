##from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from salesmen.models import Task, Employee, Responsibility
from salesmen.serializers import TaskSerializer, EmployeeSerializer, ResponsibilitySerializer

class TaskList(APIView):

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def delete(self, request, format=None):
        for x in request.data:
            task = self.get_object(x)
            task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, format=None):
        task = self.get_object(request.data['taskId'])
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def delete(self, request, format=None):
        for x in request.data:
            employee = self.get_object(x)
            employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
        data_to_send = []
        employees = Employee.objects.all()
        print(employees)
        for e in employees:
            responsibilities = e.responsibilities
            responsibility_serializer = TaskSerializer(responsibilities, many=True)
            employee_serializer = EmployeeSerializer(e)
            for x in  responsibility_serializer.data:
               to_send = {'employee': employee_serializer.data['name'], 'task': x['task_text']}
               data_to_send.append(to_send)
        print(data_to_send) 
        return Response(data_to_send)

    def post(self, request, format=None):
        employees = request.data[0]
        tasks = request.data[1]
        array_to_serialize = []
        for x in employees:
            for y in tasks:
                array_to_serialize.append({'emoployee':x, 'task':y})
        serializer = ResponsibilitySerializer(data=array_to_serialize, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)