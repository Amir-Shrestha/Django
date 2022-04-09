from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_method, name="home"),
    path('register/', views.register_method, name="register_path"),
    path('log/', include('django.contrib.auth.urls')),
]
