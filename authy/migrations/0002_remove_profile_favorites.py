# Generated by Django 3.1.3 on 2020-11-24 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favorites',
        ),
    ]
