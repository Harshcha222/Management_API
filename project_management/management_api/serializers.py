from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

# Client serializer
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'description']

# Project serializer
class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'client', 'users']
