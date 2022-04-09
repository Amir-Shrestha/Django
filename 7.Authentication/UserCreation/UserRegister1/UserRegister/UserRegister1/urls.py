from django.urls import path
from . views import register_user_1, register_user_1_1_crispy_form

urlpatterns = [
    path('', register_user_1, name="register_user_1"),
]
