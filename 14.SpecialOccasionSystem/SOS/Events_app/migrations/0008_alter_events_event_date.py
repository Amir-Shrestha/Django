# Generated by Django 3.2.5 on 2021-07-06 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Events_app', '0007_alter_events_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]