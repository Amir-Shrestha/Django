from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="admins_folder")
    mobile = models.CharField(max_length=20)

    def _str_(self):
        return self.user.username



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name






class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title






class Product(models.Model):  # M-N
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products_folder")
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    desciption = models.TextField()
    warranty = models.CharField(max_length=300, null=True, blank=True)
    return_policy = models.CharField(max_length=300, null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title






class Cart(models.Model): # M-N
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart_Id: " + str(self.id)






class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) # object of cart class, 1-M . Its mainly relationship of this CartProduct class with Cart class # Foreign key/ Primany key of another class
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # object of product class, 1-M. Its mainly relationship of this CartProduct class with Product class # Foreign key/ Primany key of another class
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    sub_total = models.PositiveIntegerField()

    def __str__(self):
        return "Cart_Id: " + str(self.cart.id) + "| Product: " + str(self.product.id) + "| Cart_Product: " + str(self.id)






# tuple of tuple # Constant # CharField as select_field
ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("Order on the way", "Order on the way"),
    ("Order Delivered", "Order Delivered"),
    ("Order Cancelled", "Order Cancelled"),
)

PAYMENT_METHOD = (
    ("Cash on delivery", "Cash on delivery"),
    ("Khalti", "Khalti"),
    ("Esewa", "Esewa"),
    ("PayPal", "PayPal"),
)

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    order_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    sub_total = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, default="Cash on delivery")
    payment_done = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return "Order_Id: " + str(self.id)



