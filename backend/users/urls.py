from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.getUsers, name="users"),
    path('users/create/', views.createUser, name='createUser')
]

