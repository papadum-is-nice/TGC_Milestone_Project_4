# Generated by Django 2.2.6 on 2020-02-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitars',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
