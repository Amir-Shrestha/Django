from django.urls import path
from . views import register_user_1_1_crispy

urlpatterns = [
    path('', register_user_1_1_crispy, name="register_user_1_1_crispy"),
]
