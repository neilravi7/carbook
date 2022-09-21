from account.models import Profile
from booking.models import Booking
from vehicle.models import Vehicle
from rest_framework import serializers, generics
from .serializers import VehicleSerializer 
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.
    

class VehicleAPIList(generics.ListAPIView):
    permission_classes = [AllowAny]

    queryset = Vehicle.objects.filter()
    serializer_class = VehicleSerializer


class VehicleAPIDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleAPIAdminView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
