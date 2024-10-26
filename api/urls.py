from .views import home
from django.urls import path
# api/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet  # Import the UserViewSet
from .views import user_list, add_user, edit_user, delete_user, client_list, add_client, edit_client, delete_client, project_list, add_project
from . import views  # Import views from the current directory
from django.contrib.auth import views as auth_views
from .views import user_login
from .views import CustomLoginView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls
# api/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ClientViewSet, ProjectViewSet  # Import all your viewsets

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('', home, name='home'),
    path('users/', user_list, name='user_list'),
    path('users/add/', add_user, name='add_user'),
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
    path('clients/', client_list, name='client_list'),
    path('clients/add/', add_client, name='add_client'),
    path('clients/edit/<int:client_id>/', edit_client, name='edit_client'),
    path('clients/delete/<int:client_id>/', delete_client, name='delete_client'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:project_id>/', views.project_details, name='project_details'),  # Corrected line
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', user_login, name='login'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('login/', CustomLoginView.as_view(), name='login'),

    path('projects/<int:project_id>/', views.project_details, name='project_details'),
]

