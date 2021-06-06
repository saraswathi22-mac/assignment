from django.db.models.query import QuerySet
from rest_framework import generics
from rest_framework.response import Response
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework.views import APIView
# Create your views here.

class Projects(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    template_name = 'home.html'

class Tasks(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()