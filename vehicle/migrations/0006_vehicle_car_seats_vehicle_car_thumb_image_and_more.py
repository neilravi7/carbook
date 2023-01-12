# Generated by Django 4.0.7 on 2022-10-18 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0005_alter_vehicle_sub_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='car_seats',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_thumb_image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='car_white_image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='engine_power',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='extra_km_charge',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='price_per_day',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='price_per_hour',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='price_per_week',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]