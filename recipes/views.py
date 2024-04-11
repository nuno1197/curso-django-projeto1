from django.http import HttpResponse
#from django.shortcuts import render

#HTTP REQUEST <- HTTP RESPONSE

#HTTP REQUEST

# Create your views here.
def home(request):
    return HttpResponse("HOME")
    #return HTTP RESPONSE


    
def contato(request):
    return HttpResponse("CONTATO")
    #return HTTP RESPONSE

    
def sobre(request):
    return HttpResponse("SOBRE")
    #return HTTP RESPONSE