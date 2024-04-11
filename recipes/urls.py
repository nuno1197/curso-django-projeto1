from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from recipes.views import home

#HTTP REQUEST <- HTTP RESPONSE

#HTTP REQUEST


#dominio/recipes/
urlpatterns = [
    path('', home), # Home
]
