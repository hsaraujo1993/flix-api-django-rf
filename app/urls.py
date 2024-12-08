"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from tkinter.font import names

from django.contrib import admin
from django.urls import path
from genres.views import GenreListCreateAPIView, GenreRetrieveUpdateDestroyAPIView
from actors.views import ActorListCreateAPIView, ActorRetrieveUpdateDestroyAPIView



urlpatterns = [

    path('admin/', admin.site.urls),
    path('genres/', GenreListCreateAPIView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre-retrieve-update-destroy'),

    path('actors/', ActorListCreateAPIView.as_view(), name='actor-list-create'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyAPIView.as_view(), name='actor-retrieve-update-destroy'),
]
