from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm,AccountForm



def loginview(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.info(request,"Username or password is incorrect")
            
    return render(request,'login.html')




def registration(request):
    if request.method=='POST':
       user_form=UserForm(request.POST)
       account_form=AccountForm(request.POST)
       if user_form.is_valid() and account_form.is_valid():
           user=user_form.save()
           print(user.username)
           profile=account_form.save(commit=False)
           profile.user=user
           profile.save()
           messages.success(request,'Account is created')
           return redirect('login')
    else:
        user_form = UserForm
        account_form=AccountForm
        messages.success(request,'Account is created')
    return render(request,'registration.html', context={'user_form':user_form,'account_form':account_form})

def logoutview(request):
    logout(request)
    return redirect('login')