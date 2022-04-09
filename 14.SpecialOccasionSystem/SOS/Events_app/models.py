from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

# CATEGORIES_CHOICES = (
#     ('gadgets','Gadgets'),
#     ('food', 'Food'),
#     ('travel','Travel'),
#     ('entertainment','Entertainment'),
#     ('study','Study'),
#     ('session','Session'),
# )

# class Event(models.Model):
#     event_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=50)
#     description = models.TextField(max_length=150)
#     event_date = models.DateTimeField(default=timezone.now)
#     # created_date = models.DateTimeField(default=timezone.now)
#     # published_date = models.DateTimeField(blank=True, null=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     published_date = models.DateTimeField(auto_now=True, null=True)
#     thumbnail = models.ImageField(upload_to="events_app/images", default="")
#     category = models.CharField(max_length=50, default="")
#     # category = models.CharField(max_length=50, choices=CATEGORIES_CHOICES, default='')
#     author = models.ForeignKey(User, on_delete=models.CASCADE, default="")

#     def __str__(self):
#         return self.title

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    event_date = models.DateTimeField(default=timezone.now)
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True, null=True)
    thumbnail = models.ImageField(upload_to="events_app/event_thumbnail", default="")
    category = models.CharField(max_length=50, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="Anonymous")

    def __str__(self):
        return self.title


class Contact(models.Model):
    SN = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=15)
    address = models.CharField(max_length=30, default="")
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from " + " - " + self.email



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="Anonymous", related_name='Profile')
    profile_id = models.AutoField(primary_key=True)
    profile_img = models.ImageField(upload_to="events_app/author_profile_img", default="default.jpg")
    cover_img = models.ImageField(upload_to="events_app/author_profile_img", default="default.jpg")

    def __str__(self):
        return f'{self.user.username} Profle '