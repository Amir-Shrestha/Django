from django.contrib import admin
from .models import Event, Contact, Profile

# Register your models here.
# admin.site.register(Model_Nmae)

@admin.register(Event)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['event_id', 'title', 'event_date', 'created_date', 'published_date', 'category', 'author']
    # list_display = ['event_id', 'title', 'event_date', 'created_date', 'published_date', 'category', 'author', 'thumbnail', 'description']


@admin.register(Contact)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['SN', 'name', 'email', 'number', 'address', 'message', 'timeStamp']

@admin.register(Profile)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_id', 'profile_img', 'cover_img']
