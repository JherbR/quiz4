from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password

@api_view(['GET'])
def getUsers(request):
    user = CustomerUserModel.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        hashed = make_password(serializer.validated_data['password'])
        serializer.save(password=hashed)
        return Response(serializer.data)
    return Response(serializer.errors)
