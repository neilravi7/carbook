from faker import Faker
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

faker = Faker()

class Vehicle(models.Model):
    AUTOMATIC = 'AUTOMATIC'
    MANUAL = 'MANUAL'

    TRANSMISSION_CHOICES = (
        (AUTOMATIC, 'Automatic'),
        (MANUAL, 'Manual'),
    )

    car_name = models.CharField(max_length=200)
    transmission = models.CharField(
        max_length=100, choices=TRANSMISSION_CHOICES, null=True, blank=True)
    descriptions = models.TextField()
    car_seats = models.CharField(max_length=20, default=0)
    fuel_type = models.CharField(max_length=20, blank=True, null=True)
    engine_power = models.CharField(max_length=20, default=0)    
    vehicle_class = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)  # car, suv and mini truck etc
    price_per_hour = models.CharField(max_length=20, blank=True, null=True)
    price_per_day = models.CharField(max_length=20, blank=True, null=True)
    price_per_week = models.CharField(max_length=20, blank=True, null=True)
    extra_km_charge = models.CharField(max_length=20, blank=True, null=True)
    sub_total_price = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    features = ArrayField(models.TextField(), blank=True, null=True)
    manufactured_by = models.CharField(max_length=50)
    manufactured_year = models.CharField(max_length=20, blank=True, null=True)
    car_white_image = models.TextField(blank=True, null=True)
    car_thumb_image = models.TextField(blank=True, null=True)
    car_photo = models.TextField(blank=True, null=True)
    car_photo = models.TextField()
    rating_count = models.PositiveIntegerField(default=0)
    star_rating = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.car_name

    def __save__(self, *args, **kwargs):
        self.descriptions = faker.text()
        super(Vehicle, self).save(*args, **kwargs)

    class Meta:
        db_table = "vehicle"