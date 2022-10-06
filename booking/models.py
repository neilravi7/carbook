from django.db import models
from django.conf import settings
from vehicle.models import Vehicle
from django.utils import timezone
from random import randint

# Create your models here.
city_list = ['Jaipur', "Udaipur", "Indore", "Bhopal", "Ahmedabad"]

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_bookings')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle_bookings')
    pick_up_address = models.TextField(null=True, blank=True)
    origin_city = models.CharField(max_length=50, null=True, blank=True)
    duration_start = models.DateTimeField()
    duration_end = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    total_amount = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{user.first}'
    class Meta:
        db_table = "booking"
    
    def __save__(self, *args, **kwargs):
        self.origin_city = city_list[randint(0,len(city_list)-1)]
        super(Booking, self).save(*args, **kwargs)
    