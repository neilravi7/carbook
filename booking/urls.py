from django.urls import path
from . import views

app_name = 'booking'
urlpatterns=[
    path('create.json/', views.CreateBookingAPI.as_view(), name="crete_booking")
]