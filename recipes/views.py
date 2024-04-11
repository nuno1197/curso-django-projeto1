
from django.shortcuts import render

#HTTP REQUEST <- HTTP RESPONSE

#HTTP REQUEST

# Create your views here.
def home(request):
    return render(request , 'recipes/pages/home.html', context={
        'name' : 'Nuno Silva'
    })
    #return HTTP RESPONSE


