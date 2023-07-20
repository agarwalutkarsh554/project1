from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse('<h1>Blog-Home</h1>')
def About(request):
    return HttpResponse('<h1>About</h1>')



# Create your views here.
