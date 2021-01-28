from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import  ModelForm
from .models import Account
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=250)
    username=forms.CharField(max_length=250)
    codeforcesid=forms.CharField(max_length=250)
    uvaid=forms.CharField(max_length=250)
    githubid=forms.CharField(max_length=250)
    
    class meta:
        model=Account
        fields= (
            'email',
            'username',
            'codeforcesid',
            'uvaid',
            'githubid',
            'password1',
            'password2',
         )   