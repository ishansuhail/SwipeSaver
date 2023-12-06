# Generated by Django 4.2.2 on 2023-12-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barh', '0002_alter_rating_station'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='meal_time',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], default='dinner', max_length=10),
        ),
    ]
