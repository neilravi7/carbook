from django.db import models
from django.conf import settings
from vehicle.models import Vehicle
from django.utils import timezone

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_bookings')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle_bookings')
    duration_start = models.DateTimeField()
    duration_end = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return f'{user.first}'
    class Meta:
        db_table = "booking"