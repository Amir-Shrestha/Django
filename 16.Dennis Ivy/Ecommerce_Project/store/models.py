from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    # email = user.email

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to="store/images", default="", null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def image_Url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    cart_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "Cart: " + str(self.id)

    @property
    def cart_total_amount(self):
        print('apple')
        cart_items = self.orderproduct_set.all()
        print([item.item_subtotal for item in cart_items])
        total_amount = sum([item.item_subtotal for item in cart_items])
        return total_amount

    @property
    def cart_total_items_quantity(self):
        print('vbaall')
        cart_items = self.orderproduct_set.all()
        total_quantity = sum([item.quantity for item in cart_items])
        return total_quantity




class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Cart_Id:" + str(self.cart.id) + ", by Customer:" + self.cart.customer.name + ", Product:" + self.product.name

    @property
    def item_subtotal(self):
        total = self.product.price * self.quantity
        return total




class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
