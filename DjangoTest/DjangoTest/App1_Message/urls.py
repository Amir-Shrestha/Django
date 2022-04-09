from django.urls import path,include
from . import views

urlpatterns = [
    path('message1/', views.message1, name='message1'),
    path('message2/', views.message2, name='message2'),
]

