from django.db import models

# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    
    def __str__(self):
        return f'Address: {self.address}, {self.city}, {self.country}, {self.postal_code}'

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Customer:{self.first_name} {self.last_name} {self.email}'

class VehicleType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class VehicleSize(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    real_cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Vehicle Type:{self.vehicle_type}, size:{self.size}, cost:{self.real_cost} and the date registered: {self.date_created}'

class Rental(models.Model):
    rental_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Rental of: {self.customer}, vehicle: {self.vehicle}, on date: {self.date_date}, due to return at: {self.return_date}'

class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits=5, decimal_places=2)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Daily rate: {self.daily_rate} for type: {self.vehicle_type} and size: {self.vehicle_size}'

class RentalStation(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Rental station: {self.name}, cap: {self.capacity}, address: {self.address}'

class VehicleAtRentalStation(models.Model):
    arrival_date = models.DateTimeField()
    departure_date = models.DateField(null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Vehicle: {self.vehicle}, arrival date: {self.arrival_date}, departure date: {self.departure_date}'


