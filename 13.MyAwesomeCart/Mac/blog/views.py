from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.

def blogIndex(request):
    posts = Blog.objects.all()
    return render(request, 'blog\index.html', {'posts':posts})

def blogPost(request, post_id):
    posts = Blog.objects.filter(post_id=post_id)
    return render(request, 'blog\post.html', {'post':posts[0]})