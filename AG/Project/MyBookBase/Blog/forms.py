from django import forms #here forms is module and ModelForm, Form are classes
from .models import Post, Document, Comment, Account
# from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm): #here ModelForm is a helper_class that helps to create form of the registered models_class.
	class Meta:
		model = Post
		fields = ('title', 'text','document')

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = ('title', 'document')


class SubscribeForm(forms.Form): #Form_API
	Email = forms.EmailField()


class CommentForm(forms.ModelForm): #ModelForm
	class Meta:
		model = Comment
		fields = ('name', 'email', 'comment_body')


# class RegisterForm(UserCreationForm):
# 	pass

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Account
        fields = ["username", "profile"]
        # fields = ["username", "email", "profile"]


# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ["username", "email"]

