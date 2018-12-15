from django.db import models

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

class Employee(models.Model):
    tasks = models.ManyToManyField(Task, blank=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
