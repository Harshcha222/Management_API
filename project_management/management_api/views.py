from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt


# Home page
def home(request):
    return HttpResponse('<h1>Welcome to Project Management System!</h1>')


# User Login (JWT Token)
@api_view(['POST'])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# Register Client (Only authenticated users)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_client(request):
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            client = serializer.save()
            return Response({"message": "Client created successfully", "client_id": client.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2. Fetch all clients (Only authenticated users)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def get_clients(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


# 3. Edit/Delete client info (Only authenticated users)
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def modify_client(request, client_id):
    try:
        client = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Client updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response({"message": "Client deleted successfully"})


# 4. Add new projects for a client and assign users (Only authenticated users)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def add_project(request):
    if request.method == 'POST':
        client = Client.objects.get(id=request.data.get('client_id'))
        project = Project.objects.create(
            name=request.data.get('name'),
            client=client
        )
        users = User.objects.filter(id__in=request.data.get('user_ids'))
        project.users.set(users)
        project.save()
        return Response({"message": "Project created and users assigned"}, status=status.HTTP_201_CREATED)


# 5. Retrieve assigned projects to logged-in users (Only authenticated users)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def get_user_projects(request):
    if request.method == 'GET':
        user = request.user
        projects = user.projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
