# Generated by Django 2.2.6 on 2020-02-29 09:34

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('checkout', '0002_delete_charge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('street_address1', models.CharField(max_length=40)),
                ('street_address2', models.CharField(max_length=40)),
                ('town_or_city', models.CharField(max_length=40)),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
    ]
