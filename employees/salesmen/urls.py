from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.TaskList.as_view(), name='task_list'),
    path('employees', views.EmployeeList.as_view(), name='employee_list')
]
