from django.db import models

# Create your models here.
class Blog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head = models.CharField(max_length=50, default="")
    content = models.CharField(max_length=5000, default="")
    publish_date = models.DateField()
    thumbnail = models.ImageField(upload_to="blog/images", default="") #this create blog/images in media

    def __str__(self):
        return self.title

