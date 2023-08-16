from rest_framework import serializers
from .models import Customer, Vehicle, VehicleType, VehicleSize, Rental, RentalRate, RentalStation, Address, VehicleAtRentalStation

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'

class VehicleSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSize
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

class RentalRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalRate
        fields = '__all__'

class RentalStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalStation
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class VehicleAtRentalStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleAtRentalStation
        fields = '__all__'
