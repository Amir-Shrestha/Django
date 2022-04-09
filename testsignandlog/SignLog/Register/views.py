from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def home_method(response):
    return render(response, 'register/home.html')

def register_method(response):
    if response.method == "POST":
        new_rgister = RegisterForm(response.POST)
        if new_rgister.is_valid():
            new_rgister.save()
            return redirect('register_path',{'msg':msg})

    form = RegisterForm()
    return render(response, 'register/signup.html', {'form':form})
