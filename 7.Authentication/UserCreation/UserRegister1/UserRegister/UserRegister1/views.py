from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.

def register_user_1(request):
    if request.method == "POST":
        new_rgister = UserCreationForm(request.POST)
        if new_rgister.is_valid():
            new_rgister.save()
            return HttpResponse('New User Registered !')
    signup_form = UserCreationForm()
    return render(request, 'register_user_1.html', {'signup_form':signup_form})