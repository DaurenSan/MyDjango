from rest_framework import serializers
from .models import Task, Employee, Responsibility

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task_text', 'pub_date', 'deadline')

class ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibility
        fields = ('emoployee', 'task', 'date_accomplished')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'phone')
