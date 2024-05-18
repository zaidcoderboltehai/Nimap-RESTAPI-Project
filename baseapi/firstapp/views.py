from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer,ClientSerializer,ProjectSerializer
from .models import Client,Project

class UserView(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class ClientView(viewsets.ModelViewSet):
    serializer_class=ClientSerializer
    queryset=Client.objects.all()

class ProjectView(viewsets.ModelViewSet):
    serializer_class=ProjectSerializer
    queryset=Project.objects.all()
