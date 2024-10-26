from django.contrib import admin
from django.urls import path, include
from api import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),         # Admin URL
    path('', views.home, name='home'),       # Home page URL
    path('api/', include('api.urls')),       # Include URLs from the api app
]
