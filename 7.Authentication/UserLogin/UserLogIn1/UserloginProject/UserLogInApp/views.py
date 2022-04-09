from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.

def user_login(request):
    if request.method=="POST":
        username1 = request.POST["uname"]
        password1 = request.POST["upass"]
        user = authenticate(username=username1, password=password1) #return Object of default User Class Model if exist else return None
        if user is not None:
            login(request, user)
            return HttpResponse("Logged In Successfully as " + str(user))
        else:
            return HttpResponse("No user with provided credentials ! !")
    return render(request, 'login.html')