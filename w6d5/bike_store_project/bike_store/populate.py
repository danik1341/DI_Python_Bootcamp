import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
import django
django.setup()

from rent.models import Customer, Address, RentalStation
from faker import Faker

fake = Faker()

def create_customers(number):
    for _ in range(number):
        address = Address(
            address=fake.street_address(),
            address2=fake.secondary_address(),
            city=fake.city(),
            country=fake.country(),
            postal_code=fake.zipcode()
        )
        address.save()

        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone_number=fake.phone_number(), 
            address=address
        )
        customer.save()

    print(f"CREATED {number} Customers")

def create_rental_stations(number):
    for _ in range(number):
        station = RentalStation(
            name=fake.street_address(),
            capacity=fake.random_int(min=1, max=100),
            address=Address.objects.create(
                address=fake.street_address(),
                address2=fake.secondary_address(),
                city=fake.city(),
                country=fake.country(),
                postal_code=fake.zipcode()
            )
        )
        station.save()

    print(f"CREATED {number} Rental Stations")

create_customers(100)
create_rental_stations(20)