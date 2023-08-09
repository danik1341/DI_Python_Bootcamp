from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.display_all_animals, name='animals-list'),
    path('families/', views.display_all_families, name='families-list'),
    path('animal/<int:pk>/', views.display_one_animal, name='animal-detail'),
    path('animal_in_family/<int:pk>/', views.display_animal_per_family, name='animal-in-family-detail'),
]
