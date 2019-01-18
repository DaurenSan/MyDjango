from datetime import datetime, timezone, timedelta
from salesmen.models import Task, Employee

def create_tasks():
    task = Task(task_text="go to mosque", pub_date=datetime.now(timezone.utc))
    task.deadline = task.pub_date+timedelta(hours=1)
    task.save()
    for x in range(1, 20):
        task = Task(task_text="go to mosque", pub_date=datetime.now(timezone.utc), deadline=task.deadline + timedelta(hours=1))
        task.save()


def create_employees():
    employee = Employee(name="J", phone="1-098-099-000")
    employee.save()
    for x in range(1, 10):
        employee = Employee(name=employee.name+"e", phone="1-098-099-000")
        employee.save()
