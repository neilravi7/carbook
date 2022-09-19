from django.shortcuts import render
from faker import Faker
import requests, json
from django.contrib.auth.models import User
from account.models import Profile
from booking.models import Booking
from vehicle.models import Vehicle
from rest_framework import serializers, generics
from .serializers import VehicleSerializer 
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

faker = Faker()


def import_data():
    url = "https://randomuser.me/api/?results=10"
    response = json.loads(requests.get(url).content)
    
    for random_user in response['results']:
        # create user object
        user_name =faker.user_name()
        fake_password = faker.password()
        
        user = User.objects.create(
            email=random_user['email'],
            username=faker.user_name(),
            first_name=random_user['name']['first'],
            last_name=random_user['name']['last']
        )

        
        user.set_password(fake_password)
        user.save()
        
        # Creating Profile
        Profile.objects.create(
            user=user,
            age=random_user['dob']['age'],
            image=random_user['picture']['large'],
            document_type="AADHAR",
            document_ref_number=f'{random_user["id"]["name"]}_{random_user["id"]["value"]}',
            address=faker.address(),
            zip_code =faker.zipcode(),
            email_confirmed=True
        )
        
        print({"username":user_name, "password":fake_password})

def import_car_data():
    url = "https://index.getaround.com/v1.0/search?product=web&properties=car_id,car_name,car_photo_v2,category,class,distance,postcode,latitude,longitude,market_abbreviation,timezone,year,make,model,dedicated_parking,subtotal_price,stars_rating,rating_count,is_new&sort=best&page_sort=magic&page_size=500&user_lat=40.7127753&user_lng=-74.0059728&start_time=2022-09-20T02:15:00.000Z&end_time=2022-09-20T10:15:00.000Z&viewport=40.651722266584784,-74.13145726655274,40.77377240189665,-73.88048833344727&zoom=12&use=CARSHARE"
    response = json.loads(requests.get(url).content)

    for car in response['cars']:
        car_obj = Vehicle.objects.create(
            car_name=car['car_name'],
            transmission='MANUAL',
            vehicle_class=car['class'],
            vehicle_type=car['category'],
            sub_total_price=car['subtotal_price'],
            rating_count=car['rating_count'],
            star_rating=car['stars_rating'],
            features=[
                "All-wheel drive", 
                "Automatic Transmission", 
                "GPS navigation system", 
                "Leather interior",
                "Cruise control",
                "Air conditioning",
                "Bluetooth wireless",
                "CD Player",
                "AUX/MP3 enabled",
                "Tinted windows",
            ],
            manufactured_by=car['make'],
            manufactured_year=car['year'],
            car_photo=car['car_photo_v2']
        )
        print(car_obj.car_name, 'Inserted')
    

class VehicleAPIList(generics.ListAPIView):
    permission_classes = [AllowAny]

    queryset = Vehicle.objects.filter()
    serializer_class = VehicleSerializer