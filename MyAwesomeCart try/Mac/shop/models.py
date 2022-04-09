from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default="0")
    desciption = models.CharField(max_length=300)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")
    # tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.product_name




# class Tag(models.Model):
#     name = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.name




class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=50)
    contact_email = models.CharField(max_length=50, default="")
    contact_phone  = models.CharField(max_length=70, default="")
    contact_address  = models.CharField(max_length=70, default="")
    contact_desciption = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.contact_name




class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")



class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.update_desc[0:14] + "..."