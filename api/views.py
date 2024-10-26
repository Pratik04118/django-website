from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Client, Project  # Import both Client and Project

from django.shortcuts import render, redirect  # Correctly importing functions from django.shortcuts
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

import requests
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return redirect('user_list')
    return render(request, 'add_user.html')


from django.shortcuts import render, get_object_or_404
from .models import User  # Import the User model or any model as needed


def edit_user(request, user_id):
    # Fetch user information (using get_object_or_404 for example)
    user = get_object_or_404(User, id=user_id)

    # Render the `edit_user.html` template
    return render(request, 'edit_user.html', {'user': user})

def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('user_list')


from .models import Client

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Client

@login_required
def add_client(request):
    if request.method == "POST":
        client_name = request.POST.get("client_name")
        if client_name:
            client = Client(
                client_name=client_name,
                created_by=request.user  # Ensure this captures the authenticated user
            )
            client.save()
            return JsonResponse({
                "id": client.id,
                "client_name": client.client_name,
                "created_at": client.created_at,
                "created_by": client.created_by.username,
            })
        return JsonResponse({"error": "Client name is required"}, status=400)
    return redirect("home")  # Or the appropriate view for non-POST requests

def edit_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client.client_name = request.POST.get('client_name')
        client.save()
        return redirect('client_list')
    return render(request, 'edit_client.html', {'client': client})

def delete_client(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('client_list')

from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def add_project(request):
    clients = Client.objects.all()
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        client_id = request.POST.get('client')
        project = Project.objects.create(project_name=project_name, client_id=client_id, created_by=request.user)
        users_ids = request.POST.getlist('users')
        project.users.set(users_ids)
        return redirect('project_list')
    return render(request, 'add_project.html', {'clients': clients})

# api/views.py
# api/views.py
from rest_framework import viewsets
from .models import User, Client, Project
from .serializers import UserSerializer, ClientSerializer, ProjectSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

from django.shortcuts import render
from django.http import JsonResponse

def project_list(request):
    # Your logic to fetch and return projects
    return JsonResponse({"projects": []})  # Example response

from django.shortcuts import render
from django.http import JsonResponse

def project_details(request, project_id):
    # Logic to fetch project details by project_id
    return JsonResponse({"project_id": project_id, "details": "Project details here"})  # Example response
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')  # Check if there's a "next" parameter
            if next_url:
                return redirect(next_url)  # Redirect to intended page
            return redirect('home')  # Otherwise, go to home page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'your_template_name.html'  # Specify your login template
    redirect_authenticated_user = True  # Optional: redirects authenticated users away from the login page
