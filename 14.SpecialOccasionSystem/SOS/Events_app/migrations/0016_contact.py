# Generated by Django 3.2.5 on 2021-07-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events_app', '0015_rename_events_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('SN', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]