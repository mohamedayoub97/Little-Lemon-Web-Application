# Generated by Django 5.1.1 on 2024-09-10 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_id',
            field=models.IntegerField(),
        ),
    ]
