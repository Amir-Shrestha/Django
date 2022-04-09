from django import forms
from .models import Order, Customer
from django.contrib.auth.models import User


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["order_by", "shipping_address", "mobile", "email", "payment_method"]


class CustomerRegistrationForm(forms.ModelForm):
    custome_username = forms.CharField(widget=forms.TextInput())
    custome_password = forms.CharField(widget=forms.PasswordInput())
    custome_email = forms.CharField(widget=forms.EmailInput())
    class Meta:
        model = Customer
        fields = ["full_name", "address"]
        # fields = ["custome_username", "custome_password", "custome_email", "full_name", "address"]

    def clean_username(self):
        instance_username = self.cleaned_data.get("custome_username")
        if User.objects.filter(username=instance_username).exists():
            raise forms.ValidationError("Customer with this username already exists !")
        return instance_username


class UserLogInForm(forms.Form):
    login_username = forms.CharField(widget=forms.TextInput())
    login_password = forms.CharField(widget=forms.PasswordInput())
