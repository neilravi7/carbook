from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class CreateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_pass = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(user_pass)
        user.save()

        Profile.objects.create(user=user)
        return user