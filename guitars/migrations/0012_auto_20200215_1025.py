# Generated by Django 2.2.6 on 2020-02-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0011_auto_20200215_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitars',
            name='prod_year',
            field=models.IntegerField(blank=True),
        ),
    ]
