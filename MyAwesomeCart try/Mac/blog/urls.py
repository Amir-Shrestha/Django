from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogIndex, name='blogIndex'),
    path('blogPost/<int:post_id>', views.blogPost, name='blogPost') #<int:post_id> to uniquely identify post
]
