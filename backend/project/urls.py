from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView)

urlpatterns = [
    path('projects/', views.getProjects, name="projects"),
    path('projects/<str:pk>', views.getProject, name="project"),
    path('projects/<str:pk', include('task.urls'))
]