# Generated by Django 2.2.6 on 2020-02-09 09:00

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0002_auto_20200209_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitars',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True, null=True),
        ),
    ]
