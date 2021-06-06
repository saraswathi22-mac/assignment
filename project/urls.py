from django.urls import path
from .views import Projects, Tasks

app_name = 'project'

urlpatterns = [
    path('<int:id>', Projects.as_view(), name="project"),
    path('task/<int:id>', Tasks.as_view(), name="task"),
]