# Generated by Django 4.0.7 on 2022-09-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_alter_vehicle_sub_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='sub_total_price',
            field=models.DecimalField(decimal_places=12, max_digits=12),
        ),
    ]
