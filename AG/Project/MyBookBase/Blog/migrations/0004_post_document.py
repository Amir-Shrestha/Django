# Generated by Django 3.2.2 on 2021-05-21 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20210521_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(default='', upload_to='blog/images/'),
        ),
    ]