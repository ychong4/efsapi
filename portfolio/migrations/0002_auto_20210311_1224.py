# Generated by Django 3.0.7 on 2021-03-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cust_number',
            field=models.CharField(max_length=50),
        ),
    ]
