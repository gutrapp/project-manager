from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Project, Developer
from .serializer import DeveloperSerializer, ProjectSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def getUsers(request):
    developers = Developer.objects.all()
    serializer = DeveloperSerializer(developers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getUser(request, id):
    try:
        developer = Developer.objects.get(id=id)
    except:
        return Response({"message": "Developer of id {} doesn't exist".format(id)}, status=status.HTTP_204_NO_CONTENT)
    
    serializer = DeveloperSerializer(developer)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createUser(request):
    serializer = DeveloperSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Developer created successfuly"}, status=status.HTTP_200_OK)
    return Response({"message": "Data provided is invalid"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['DELETE'])
def deleteUser(request, id):
    try:
        developer = Developer.objects.get(id=id)
    except:
        return Response({"message": "Developer of id {} doesn't exist".format(id)}, status=status.HTTP_204_NO_CONTENT)

    developer.delete()
    return Response({"message": "Developer deleted successfuly"}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def updateUser(request):
    serializer = DeveloperSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Developer updated successfuly"}, status=status.HTTP_200_OK)
    return Response({"message": "Data provided is invalid"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getProject(request, id):
    project = Project.objects.get(id=id)
    serializer = ProjectSerializer(project)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createProject(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Project created successfuly"}, status=status.HTTP_200_OK)
    return Response({"message": "Data provided is invalid"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['DELETE'])
def deleteProject(request, id):
    try:
        project = Project.objects.get(id=id)
    except:
        return Response({"message": "Project of id {} doesn't exist".format(id)}, status=status.HTTP_204_NO_CONTENT)
    
    project.save()
    return Response({"message": "Developer deleted successfuly"}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def updateProject(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Project updated successfuly"}, status=status.HTTP_200_OK)
    return Response({"message": "Data provided is invalid"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)