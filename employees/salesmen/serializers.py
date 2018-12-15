from rest_framework import serializers
from .models import Task
from .models import Employee

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task_text', 'pub_date')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'phone', 'tasks')
