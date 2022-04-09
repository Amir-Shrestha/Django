from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Event


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # image = forms.ImageField(upload_to="events_app/images/account_profile", default="")
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                   'first_name':forms.TextInput(attrs={'class':'form-control'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'}),
                    }

class LogInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("PassworD"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date', 'thumbnail', 'category']
        labels = {'title':'Event Title', 'description':'Event Description', 'event_date':'Event Date', 'thumbnail':'Event Thumbnail', 'category':'Event Category'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                   'description':forms.TextInput(attrs={'class':'form-control'}),
                   'event_date':forms. DateTimeInput(attrs={'class':'form-control'}),
                   'event_thumbnail':forms.FileInput(attrs={'class':'form-control'}),
                   'category':forms.TextInput(attrs={'class':'form-control'}),
                    }


class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {'email':'Email'}