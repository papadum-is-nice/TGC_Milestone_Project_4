# Generated by Django 2.2.6 on 2020-02-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0014_auto_20200215_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitars',
            name='brand',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='guitars',
            name='model',
            field=models.CharField(max_length=50),
        ),
    ]