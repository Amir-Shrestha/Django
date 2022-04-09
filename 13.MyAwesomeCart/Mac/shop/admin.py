from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Orders, OrderUpdate

@admin.register(Product)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'product_name', 'category']




admin.site.register(Contact)


@admin.register(Orders)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'items_json', 'amount', 'name', 'email', 'address', 'city', 'state', 'zip_code', 'phone']



@admin.register(OrderUpdate)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['update_id', 'order_id', 'update_desc', 'timestamp']


