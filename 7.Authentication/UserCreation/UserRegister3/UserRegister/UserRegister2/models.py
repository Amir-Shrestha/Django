from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, default="")
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, default="")
    country = models.CharField(max_length=200, default="")
    district = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    society = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=200, default="")
    age = models.CharField(max_length=200, default="")
    gender = models.CharField(max_length=200, default="")
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

