from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import get_user_model

User = get_user_model()


def login(request):
    return render(request,'login.html')

def registration(request):
    form = RegistrationForm()
    context={'form':form}
    if request.method=='POST':
       form=RegistrationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('')
    return render(request,'registration.html', context)

