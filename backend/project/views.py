from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request, pk):
    try:
        project = Project.objects.get(_id=pk)
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response({'detail': 'Product not found'}, status=404)
