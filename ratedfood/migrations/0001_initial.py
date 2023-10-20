# Generated by Django 4.2.2 on 2023-10-16 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ratedFoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ratedfood_images/')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('vegan', models.BooleanField()),
                ('dining_hall', models.CharField(default='commons', max_length=50)),
            ],
        ),
    ]
