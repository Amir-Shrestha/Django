# from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    document = models.ImageField(upload_to='blog/images/', default="")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class Document(models.Model):
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment_body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return "Comment '{}' by {}".format(self.comment_body, self.name)


class Account(User):
    profile = models.ImageField(upload_to='blog/profile_folder/', default="")