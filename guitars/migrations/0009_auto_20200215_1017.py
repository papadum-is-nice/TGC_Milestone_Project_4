# Generated by Django 2.2.6 on 2020-02-15 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0008_auto_20200213_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitars',
            name='prod_year',
            field=models.IntegerField(null=True),
        ),
    ]
