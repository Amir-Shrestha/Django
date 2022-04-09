from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('authorlist/', views.authorlist, name='authorlist'),
    path('authorlist/', views.authorlist, name='authorlist'),
    path('event/<int:event_id>', views.event, name='event'),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logot/', views.logout_user, name='logout'),
    path('create_event/', views.create_event, name='create_event'),
    path('update_event/<int:event_id>', views.update_event, name='update_event'), #dynamic_url
    path('delete_event/<int:id>', views.delete_event, name='delete_event'), #dynamic_url
]

