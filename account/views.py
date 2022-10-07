from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from . import serializers 
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class UserProfileAPI(generics.CreateAPIView):
    permission_classes = [AllowAny]
    
    queryset = User.objects.filter()
    serializer_class = serializers.CreateUserProfileSerializer

