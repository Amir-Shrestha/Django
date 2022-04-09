from django.contrib import admin
from .models import Post, Document, Comment, Account

# Register your models here.
admin.site.register(Post)
admin.site.register(Document)
admin.site.register(Comment)
admin.site.register(Account)
