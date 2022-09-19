from django.urls import path
from .views import VehicleAPIList
# AUTHENTICATION VIEWS

app_name = 'vehicle'

urlpatterns=[
    path('list/', VehicleAPIList.as_view(), name='vehicle_list'),

]

