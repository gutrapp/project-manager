from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view

@api_view(['GET'])
def getUsers(request):
    pass

@api_view(['GET'])
def getUser(request):
    pass

@api_view(['POST'])
def createUser(request):
    pass

@api_view(['DELETE'])
def deleteUser(request):
    pass

@api_view(['PUT'])
def updateUser(request):
    pass

@api_view(['GET'])
def getProjects(request):
    pass

@api_view(['GET'])
def getProject(request):
    pass

@api_view(['POST'])
def createProject(request):
    pass

@api_view(['DELETE'])
def deleteProject(request):
    pass

@api_view(['PUT'])
def updateProject(request):
    pass