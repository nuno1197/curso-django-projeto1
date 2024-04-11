from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from recipes.views import contato, home, sobre

#HTTP REQUEST <- HTTP RESPONSE

#HTTP REQUEST


#dominio/recipes/
urlpatterns = [
    path('', home), # Home
    path('/sobre', sobre), # /sobre
    path('/contacto', contato), # /contacto
]
