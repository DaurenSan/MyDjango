from rest_framework.views import APIView
from rest_framework.response import Response
##from rest_framework.renderers import JSONRenderer
##from rest_framework.parsers import JSONParser
from salesmen.models import Task
from salesmen.serializers import TaskSerializer

class TaskList(APIView):

    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)