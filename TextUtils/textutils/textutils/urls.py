"""textutils URL Configuration
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), #home page or index page
    path('analyzed', views.analyzed, name='analyzed'), #remove puntuation method
    path('nav', views.nav, name='nav'), #remove puntuation method
]


