# Generated by Django 4.0.7 on 2022-09-24 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total_amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]