from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    custome_username = forms.CharField(required=True)
    custome_password = forms.CharField(required=True)
    custome_email = forms.EmailField(required=True)
    class Meta:
        model = Customer
        fields = ["first_name", "middle_name" , "last_name", "country", "district", "city", "society", "phone", "age", "gender"]