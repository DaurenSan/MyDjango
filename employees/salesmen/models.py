from django.db import models

class Task(models.Model):
    """
    This class describes all the tasks, which we want to accomlish
    """
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    deadline = models.DateTimeField(null=True)

class Employee(models.Model):
    """
    This class describes all employees, which work for us
    """
    responsibilities = models.ManyToManyField(Task, through='Responsibility', blank=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class Responsibility(models.Model):
    """
    Actually this class describes tasks, which are assigned to employees, responsible to manage these tasks
    """
    emoployee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date_accomplished = models.DateTimeField()
