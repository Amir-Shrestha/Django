from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(default="profile.jpg", null=True, blank=True)

    def __str__(self):
        return str(self.name)+' Profile'



class Tag(models.Model):

    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name



class Product(models.Model):

    CATEGORY = (
                ('Indoor', 'Indoor'),
                ('Out Door', 'Out Door'),
            )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



class Order(models.Model):

    STATUS = (
                ('Pending', 'Pending'),
                ('Out for delivery', 'Out for delivery'),
                ('Delivered', 'Delivered'),
            )

    profile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    status1 = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=200, null=True)


    def __str__(self):
        return str(self.product) + ' is ' + str(self.status) + ' by ' + str(self.profile)
