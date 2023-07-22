from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request,'blog/home.html')
def About(request):
    return HttpResponse('<h1>About</h1>')



# Create your views here.
