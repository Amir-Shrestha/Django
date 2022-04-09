from django.shortcuts import render
from .forms import CustomerRegistrationForm
from .models import Customer
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.

def register_user_3(request):
    if request.method == "POST":
        signup_form = CustomerRegistrationForm(request.POST)
        if signup_form.is_valid():
            username1 = signup_form.cleaned_data.get("custome_username")
            password1 =  signup_form.cleaned_data["custome_password"]
            email1 =  signup_form.cleaned_data.get("custome_email")
            django_user = User.objects.create_user(username1, email1, password1)

            first_name1 =  signup_form.cleaned_data.get("first_name")
            middle_name1 =  signup_form.cleaned_data.get("middle_name")
            last_name1 =  signup_form.cleaned_data.get("last_name")
            country1 =  signup_form.cleaned_data.get("country")
            district1 =  signup_form.cleaned_data.get("district")
            city1 =  signup_form.cleaned_data.get("city")
            society1 =  signup_form.cleaned_data.get("society")
            phone1 =  signup_form.cleaned_data.get("phone")
            age1 =  signup_form.cleaned_data.get("age")
            gender1 =  signup_form.cleaned_data.get("gender")

            # customer = Customer(user=django_user, first_name=first_name1, middle_name=middle_name1, last_name=last_name1, country=country1, district=district1, city=city1, society=society1, phone=phone1, age=age1, gender=gender1)
            customer = Customer(first_name=first_name1, middle_name=middle_name1, last_name=last_name1, country=country1, district=district1, city=city1, society=society1, phone=phone1, age=age1, gender=gender1)
            customer.user = django_user
            customer.save()
            return HttpResponse('New User Registered !')
    signup_form = CustomerRegistrationForm()
    return render(request, 'register_user_3.html', {'signup_form':signup_form})
