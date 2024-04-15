from django.contrib import admin
from django.urls import path,re_path
from django.http import HttpResponse
from . import views

#HTTP REQUEST <- HTTP RESPONSE

#HTTP REQUEST


#dominio/recipes/
urlpatterns = [
    path('', views.home), # home
    path ('recipes/<int:id>/', views.recipe),
]
