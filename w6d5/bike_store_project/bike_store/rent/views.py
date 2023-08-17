from datetime import datetime
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncMonth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Customer, Vehicle, VehicleType, VehicleSize, Rental, RentalRate, RentalStation, Address, VehicleAtRentalStation
from .serializers import CustomerSerializer, VehicleSerializer, VehicleTypeSerializer, VehicleSizeSerializer, RentalSerializer, RentalRateSerializer, RentalStationSerializer, AddressSerializer, VehicleAtRentalStationSerializer

# Create your views here.

class CustomerAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            customers = Customer.objects.all()
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)
        else:
            customer = Customer.objects.get(id=pk)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, pk):
        customer_update = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(instance=customer_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        customer_delete = Customer.objects.get(id=pk)
        customer_delete.delete()
        return Response(f'Customer - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)

class VehicleAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            vehicles = Vehicle.objects.all()
            serializer = VehicleSerializer(vehicles, many=True)
            return Response(serializer.data)
        else:
            vehicle = Vehicle.objects.get(id=pk)
            serializer = VehicleSerializer(vehicle)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = VehicleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, pk):
        vehicle_update = Vehicle.objects.get(id=pk)
        serializer = VehicleSerializer(instance=vehicle_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        customer_delete = Vehicle.objects.get(id=pk)
        customer_delete.delete()
        return Response(f'Vehicle - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)

class VehicleTypeAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            vehicle_types = VehicleType.objects.all()
            serializer = VehicleTypeSerializer(vehicle_types, many=True)
            return Response(serializer.data)
        else:
            vehicle_type = VehicleType.objects.get(id=pk)
            serializer = VehicleTypeSerializer(vehicle_type)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = VehicleTypeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, pk):
        vehicle_type_update = VehicleType.objects.get(id=pk)
        serializer = VehicleTypeSerializer(instance=vehicle_type_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        vehicle_type_delete = VehicleType.objects.get(id=pk)
        vehicle_type_delete.delete()
        return Response(f'Vehicle Type - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)

class VehicleSizeAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            vehicle_sizes = VehicleSize.objects.all()
            serializer = VehicleSizeSerializer(vehicle_sizes, many=True)
            return Response(serializer.data)
        else:
            vehicle_size = VehicleSize.objects.get(id=pk)
            serializer = VehicleSizeSerializer(vehicle_size)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = VehicleSizeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, pk):
        vehicle_size_update = VehicleSize.objects.get(id=pk)
        serializer = VehicleSizeSerializer(instance=VehicleSize, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        vehicle_size_delete = VehicleSize.objects.get(id=pk)
        vehicle_size_delete.delete()
        return Response(f'Vehicle Size - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)

class RentalAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            rentals = Rental.objects.all()
            serializer = RentalSerializer(rentals, many=True)
            return Response(serializer.data)
        else:
            rental = Rental.objects.get(id=pk)
            serializer = RentalSerializer(rental)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = RentalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, pk):
        rental_update = Rental.objects.get(id=pk)
        serializer = RentalSerializer(instance=rental_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        rental_delete = Rental.objects.get(id=pk)
        rental_delete.delete()
        return Response(f'Rental - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)

class RentalRateAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            rental_rates = RentalRate.objects.all()
            serializer = RentalRateSerializer(rental_rates, many=True)
            return Response(serializer.data)
        else:
            rental_rate = RentalRate.objects.get(id=pk)
            serializer = RentalRateSerializer(rental_rate)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = RentalRateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, pk):
        rental_rate_update = RentalRate.objects.get(id=pk)
        serializer = RentalRateSerializer(instance=rental_rate_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        rental_rate_delete = RentalRate.objects.get(id=pk)
        rental_rate_delete.delete()
        return Response(f'Rental Rate - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)

class RentalStationAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            rental_stations = RentalStation.objects.all()
            serializer = RentalStationSerializer(rental_stations, many=True)
            return Response(serializer.data)
        else:
            rental_station = RentalStation.objects.get(id=pk)
            serializer = RentalStationSerializer(rental_station)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = RentalStationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, pk):
        rental_station_update = RentalStation.objects.get(id=pk)
        serializer = RentalStationSerializer(instance=rental_station_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        rental_station_delete = RentalStation.objects.get(id=pk)
        rental_station_delete.delete()
        return Response(f'Rental Station - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)

class AddressAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            addresses = Address.objects.all()
            serializer = AddressSerializer(addresses, many=True)
            return Response(serializer.data)
        else:
            address = Address.objects.get(id=pk)
            serializer = AddressSerializer(address)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = AddressSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, pk):
        address_update = Address.objects.get(id=pk)
        serializer = AddressSerializer(instance=address_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        address_delete = Address.objects.get(id=pk)
        address_delete.delete()
        return Response(f'Address - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)

class VehicleAtRentalStationAPIView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            vehicle_at_rental_stations = VehicleAtRentalStation.objects.all()
            serializer = VehicleAtRentalStationSerializer(vehicle_at_rental_stations, many=True)
            return Response(serializer.data)
        else:
            vehicle_at_rental_station = VehicleAtRentalStation.objects.get(id=pk)
            serializer = VehicleAtRentalStationSerializer(vehicle_at_rental_station)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = VehicleAtRentalStationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(arrival_date=datetime.now())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def put(self, request, pk):
        vehicle_at_rental_station_update = VehicleAtRentalStation.objects.get(id=pk)
        
        if 'departure_date' in request.data:
            vehicle_at_rental_station_update.departure_date = datetime.now()
            vehicle_at_rental_station_update.save()
            return Response({'message': 'Departure date set.'}, status=status.HTTP_200_OK)
        
        serializer = VehicleAtRentalStationSerializer(instance=vehicle_at_rental_station_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        vehicle_at_rental_station_delete = VehicleAtRentalStation.objects.get(id=pk)
        vehicle_at_rental_station_delete.delete()
        return Response(f'Vehicle At Rental Station - {pk} DELETED', status=status.HTTP_204_NO_CONTENT)

class MonthlyRentalStats(APIView):
    def get(self, request, format = None):
        rental_stats = Rental.objects.annotate(month=TruncMonth('rental_date')).values('month').annotate(count=Count('id')).order_by('month')
        
        monthly_stats = {}
        for stat in rental_stats:
            month_str = stat['month'].strftime('%Y-%m')
            monthly_stats[month_str] = stat['count']

        return Response(monthly_stats)

class PopularRentalStation(APIView):
    def get(self, request, format=None):
        popular_stations = VehicleAtRentalStation.objects.values('station__name').annotate(num_rentals=Count('vehicle')).order_by('-num_rentals')

        station_stats = {station['station__name']: station['num_rentals'] for station in popular_stations}

        return Response(station_stats)

class PopularVehicleType(APIView):
    def get(self, request, format=None):
        rented_vehicle_types = Rental.objects.values('vehicle__vehicle_type').annotate(num_rentals=Count('vehicle')).order_by('-num_rentals')

        vehicle_type_stats = {vehicle_type['vehicle__vehicle_type']: vehicle_type['num_rentals'] for vehicle_type in rented_vehicle_types}

        return Response(vehicle_type_stats)