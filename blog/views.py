from django.shortcuts import render
from django.http import HttpResponse
from .models import post#. here means that it is in the same package if it was in some other package we would have mentioned that before .
def Home(request):
    context={
        'posts':post.objects.all()
    }
    return render(request, 'blog/home.html',context)
def About(request):

    return render(request, 'blog/about.html',{'title':'About'})



# Create your views here.
