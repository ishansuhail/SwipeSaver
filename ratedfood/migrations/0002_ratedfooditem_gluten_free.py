# Generated by Django 4.2.2 on 2023-10-20 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratedfood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratedfooditem',
            name='gluten_free',
            field=models.BooleanField(default=False),
        ),
    ]
