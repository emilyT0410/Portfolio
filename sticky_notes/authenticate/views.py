from django.shortcuts import render, redirect
from django.contrib.auth import login, logout 
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.
def register_user(request):
    '''User can create account with username and password'''
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password_conf = form.cleaned_data['password_conf']
            if password == password_conf:
                new_user = User()
                new_user.username = form.cleaned_data['username']
                new_user.set_password(password)
                new_user.save()
                login(request, new_user)
                return redirect('index')
    form = RegisterForm()
    return render(request, 'registration/register.html', context={'form':form})


def logout_user(request):
    '''Allows the user to log out of their acccount'''
    logout(request)
    return redirect('index')
