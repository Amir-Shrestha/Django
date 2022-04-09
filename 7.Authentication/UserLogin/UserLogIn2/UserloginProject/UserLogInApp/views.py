from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.



# 1
def user_login(request):
    if request.method=="POST":
        login_form = AuthenticationForm(request=request, data=request.POST)
        # print(login_form)
        # print(login_form.__dict__.keys())
        if login_form.is_valid():
            username1 = request.POST["username"]
            password1 = request.POST["password"]
            user = authenticate(username=username1, password=password1) #return Object of default User Class Model if exist else return None
            if user is not None:
                login(request, user)
                return HttpResponse("Logged In Successfully !")
            else:
                return HttpResponse("No user with provided credentials ! !")
    login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form':login_form})



# # 2
# def user_login(request):
#     if request.method=="POST":
#         login_form = AuthenticationForm(request=request, data=request.POST)
#         # login_form = AuthenticationForm(request, data=request.POST)
#         if login_form.is_valid():
#             username1 = request.POST["username"]
#             password1 = request.POST["password"]
#             user = authenticate(username=username1, password=password1) #return Object of default User Class Model if exist else return None
#             if user is not None:
#                 login(request, user)
#                 return HttpResponse("Logged In Successfully !")
#             else:
#                 return HttpResponse("No user with provided credentials ! !")
#     login_form = AuthenticationForm()
#     # login_form = AuthenticationForm(request)
#     return render(request, 'login.html', {'login_form':login_form})







# # 3
# def user_login(request):
#     if request.method=="POST":
#         login_form = AuthenticationForm(request=request, data=request.POST)
#         if login_form.is_valid():
#             user = login_form.get_user()
#             if user is not None:
#                 login(request, user)
#                 return HttpResponse("Logged In Successfully !")
#             else:
#                 return HttpResponse("No user with provided credentials ! !")
#     login_form = AuthenticationForm()
#     return render(request, 'login.html', {'login_form':login_form})


