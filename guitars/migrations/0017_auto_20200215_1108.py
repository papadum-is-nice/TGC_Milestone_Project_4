# Generated by Django 2.2.6 on 2020-02-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0016_auto_20200215_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitars',
            name='prod_year',
            field=models.CharField(max_length=4),
        ),
    ]
