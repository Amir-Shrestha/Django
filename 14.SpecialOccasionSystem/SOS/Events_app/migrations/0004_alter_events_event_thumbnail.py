# Generated by Django 3.2.5 on 2021-07-06 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events_app', '0003_events_event_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_thumbnail',
            field=models.ImageField(default='', upload_to='static/events_app/images'),
        ),
    ]
