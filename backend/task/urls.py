from django.urls import path
from . import views

urlpatterns = [
    path('task/create/', views.getTasks, name="task"),
]