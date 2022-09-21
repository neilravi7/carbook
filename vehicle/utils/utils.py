from faker import Faker
import requests, json
from django.contrib.auth.models import User
from account.models import Profile
from booking.models import Booking
from vehicle.models import Vehicle


faker = Faker()


def import_data(url_string):
    url = url_string
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

def import_car_data(url_string):
    url = url_string
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