from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):

    MALE = 'MALE'
    FEMALE = 'FEMALE'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile'
    )
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.CharField(max_length=250, blank=True, null=True)
    document_type = models.CharField(max_length=70, blank=True, null=True)
    document_ref_number= models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True, help_text="Enter your address")
    zip_code = models.CharField(max_length=20, help_text="Enter your zipcode", blank=True, null=True)
    email_confirmed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        f"{self.user.username}'s Profile"