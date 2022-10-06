from rest_framework import serializers
from .import models

class BookingAdminSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = ['user', 'vehicle', 'pick_up_address', 'origin_city', 'duration_start', 'duration_end', 'total_amount']


# class BookingCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Booking
#         fields = ['vehicle', 'duration_start', 'duration_end', 'total_amount']