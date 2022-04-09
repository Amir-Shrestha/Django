from django.urls import path,include
from . import views

urlpatterns = [
    # path('', views.blogindex, name='blogindex'),
    path('', views.post_list, name='post_list'),
    path('a_post/<int:post_id>', views.a_post, name='apost'),
    path('new_post', views.create_post, name='create_post'),
    path('add_file', views.upload, name='add_file'),
    path('email_subscribe', views.subscribe, name='email_subscribe'),
    # path('about', views.about, name='blogabout'),
    path('register/', views.register_method, name="register_path"),
    path('log/', include('django.contrib.auth.urls')),
]

