from django.forms import ModelForm
from .models import Order, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


