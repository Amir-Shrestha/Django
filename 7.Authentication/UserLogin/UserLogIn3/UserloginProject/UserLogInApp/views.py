from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import Custome_User_AuthenticationForm
# Create your views here.

def user_login(request):
    if request.method=="POST":
        login_form = Custome_User_AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            if user is not None:
                login(request, user)
                return HttpResponse("Logged In Successfully !")
            else:
                return HttpResponse("No user with provided credentials ! !")
    login_form = Custome_User_AuthenticationForm(request)
    return render(request, 'login.html', {'login_form':login_form})


