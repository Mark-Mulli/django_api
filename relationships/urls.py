"""
URL configuration for relationships project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main_app import views

urlpatterns = [
    path('', views.show, name="home"),
    path('api/artists',views.api_artists, name='api_artists'),
    path('api/artists/<int:pk>',views.api_single_artists, name='api_artists'),
    path('api/artists/<int:pk>/delete',views.api_delete_artists, name='api_delete_artists'),
    path('api/artists/<int:pk>/update',views.api_update_artists, name='api_update_artists'),
    path('api/artists/<int:pk>/albums', views.api_albums_artists, name='api_albums_artists'),
    path('admin/', admin.site.urls),
]
