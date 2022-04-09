from django.shortcuts import render
from .forms import UserCreationCrispyForm
from django.http import HttpResponse

# Create your views here.

def register_user_1_1_crispy(request):
    if request.method == "POST":
        new_rgister = UserCreationCrispyForm(request.POST)
        if new_rgister.is_valid():
            new_rgister.save()
            return HttpResponse('New User Registered !')
    signup_form = UserCreationCrispyForm()
    return render(request, 'register_user_1_1_crispy.html', {'signup_form':signup_form})