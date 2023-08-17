"""
URL configuration for bike_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rent.views import (
    CustomerAPIView, 
    VehicleAPIView, 
    VehicleTypeAPIView, 
    VehicleSizeAPIView, 
    RentalAPIView, 
    RentalRateAPIView, 
    RentalStationAPIView, 
    AddressAPIView, 
    VehicleAtRentalStationAPIView, 
    MonthlyRentalStats,
    PopularRentalStation,
    PopularVehicleType,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('rent/customer/', CustomerAPIView.as_view(), name='customer-operations'),
    path('rent/customer/<int:pk>/', CustomerAPIView.as_view(), name='customer-detail'),

    path('rent/vehicle/', VehicleAPIView.as_view(), name='vehicle-operations'),
    path('rent/vehicle/<int:pk>/', VehicleAPIView.as_view(), name='vehicle-detail'),

    path('rent/vehicle-type/', VehicleTypeAPIView.as_view(), name='vehicle-type-operations'),
    path('rent/vehicle-type/<int:pk>/', VehicleTypeAPIView.as_view(), name='vehicle-type-detail'),

    path('rent/vehicle-size/', VehicleSizeAPIView.as_view(), name='vehicle-size-operations'),
    path('rent/vehicle-size/<int:pk>/', VehicleSizeAPIView.as_view(), name='vehicle-size-detail'),

    path('rent/rental/', RentalAPIView.as_view(), name='rental-operations'),
    path('rent/rental/<int:pk>/', RentalAPIView.as_view(), name='rental-detail'),

    path('rent/rental-rate/', RentalRateAPIView.as_view(), name='rental-rate-operations'),
    path('rent/rental-rate/<int:pk>/', RentalRateAPIView.as_view(), name='rental-rate-detail'),

    path('rent/rental-station/', RentalStationAPIView.as_view(), name='rental-station-operations'),
    path('rent/rental-station/<int:pk>/', RentalStationAPIView.as_view(), name='rental-station-detail'),

    path('rent/address/', AddressAPIView.as_view(), name='address-operations'),
    path('rent/address/<int:pk>/', AddressAPIView.as_view(), name='address-detail'),

    path('rent/vehicle-at-rental-station/', VehicleAtRentalStationAPIView.as_view(), name='vehicle-at-rental-station-operations'),
    path('rent/vehicle-at-rental-station/<int:pk>/', VehicleAtRentalStationAPIView.as_view(), name='vehicle-at-rental-station-detail'),
    
    path('rent/stats/monthly/', MonthlyRentalStats.as_view(), name='monthly-rental-stats'),
    path('rent/stats/popular_station/', PopularRentalStation.as_view(), name='popular-rental-station'),
    path('rent/stats/popular_vehicle_type/', PopularVehicleType.as_view(), name='popular-vehicle-type-stats'),
]
