# Generated by Django 3.2.19 on 2023-10-10 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('russellsage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
