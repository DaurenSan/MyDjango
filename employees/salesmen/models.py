from django.db import models

class Task(models.Model):
    """
    Этот класс описывает задания. которые у нас в работе
    """
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)

class Employee(models.Model):
    """
    Этот класс описывает работников, которые работают на нас
    """
    responsibilities = models.ManyToManyField(Task, through='Responsibility', blank=True)
    name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)

class Responsibility(models.Model):
    """
    Этот класс описывает задания, которые непосредственно поручены к выполнению определенным сотрудникам
    """
    emoployee = models.ForeignKey(Employee, on_delete=models.CASCADE,)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date_accomplished = models.DateTimeField(null=True)
