from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:# it is an internal class which we use when we want to mdify our model in this case User
        model=User
        fields= ['username','email','password1','password2']
