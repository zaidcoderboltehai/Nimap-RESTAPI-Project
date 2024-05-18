from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client,Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username"]

class ClientSerializer(serializers.ModelSerializer):
    Project_details=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    profile_pic=serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model=Client
        fields="__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields="__all__"