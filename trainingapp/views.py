from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from .forms import registrationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction


def home(request):
    return render(request,'forms/home.html')

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = registrationForm(request.POST)
        print form
        if form.is_valid():
            user = form.save()
            # user.refresh_from_db()
            username = form.cleaned_data.get('username')
            # user.profile.bith_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return render(request,'forms/home.html',{'user':user})
    else:
        form = registrationForm()
    return render(request,'forms/registration.html',{'form':form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        print username
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return render(request,'forms/home.html',{'user':user})
            else:
                return render(request,'forms/login.html',{'error_message':'User is disabled'})
        else:
            return render(request,'forms/login.html',{'error_message':'Invalid Login, Please enter the valid inforamtion'})
    return render(request,'forms/login.html')

def logout_user(request):
    logout(request)
    form = registrationForm(request.POST or None)
    # context = {
    #     "form":form
    # }
    return render(request,'forms/login.html',{'form':form})