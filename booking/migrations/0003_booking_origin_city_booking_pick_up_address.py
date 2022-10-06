# Generated by Django 4.0.7 on 2022-09-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='origin_city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='pick_up_address',
            field=models.TextField(blank=True, null=True),
        ),
    ]