from django.contrib import admin
from .models import Profile,Product,Order,Tag

# Register your models here.

# admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)

@admin.register(Profile)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'name', 'phone', 'email', 'date_created', 'profile_pic']
