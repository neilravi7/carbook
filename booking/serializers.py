from rest_framework import serializers
from .import models

class BookingAdminSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'


class BookingSerializerUser(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = ['vehicle', 'duration_start', 'duration_end']