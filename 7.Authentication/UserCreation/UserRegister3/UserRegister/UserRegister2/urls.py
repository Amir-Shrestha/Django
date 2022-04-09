from django.urls import path
from . views import register_user_3

urlpatterns = [
    path('', register_user_3, name="register_user_3"),
]
