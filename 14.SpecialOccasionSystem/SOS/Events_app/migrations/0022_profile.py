# Generated by Django 3.2.5 on 2021-07-23 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Events_app', '0021_alter_event_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_img', models.ImageField(default='default.svg', upload_to='events_app/author_profile_img')),
                ('user', models.OneToOneField(default='Anonymous', on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
