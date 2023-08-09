from django.http import HttpResponse
from django.shortcuts import render
from .data import animals, families

# Create your views here.


def display_all_animals(request):
    animals_info = []
    for animal in animals:
        animal_info = f"Name {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, Height: {animal['height']}, Speed: {animal['speed']}"
        animals_info.append(animal_info)
    response_content = '\n'.join(animals_info)
    return HttpResponse(response_content)


def display_all_families(request):
    family_names = [family['name'] for family in families]
    response_content = '\n'.join(family_names)
    return HttpResponse(response_content)

def display_one_animal(request, animal_id):
    selected_animal = next((animal for animal in animals if animal['id'] == animal_id), None)
    
    if selected_animal:
        animal_info = f"Name: {selected_animal['name']}, Legs: {selected_animal['legs']}, Weight: {selected_animal['weight']}, Height: {selected_animal['height']}, Speed: {selected_animal['speed']}"
        return HttpResponse(animal_info)
    else: 
        return HttpResponse("Animal not found.")
    

def display_animal_per_family(request, family_id):
    selected_family = next((family for family in families if family['id'] == family_id), None)
    
    if selected_family:
        family_animals = [animal for animal in animals if animal['family'] == selected_family['id']]
        
        if family_animals:
            animals_info = []
            for animal in animals:
                animal_info = f"Name: {animal['name']}, Legs: {animal['legs']}, Weight: {animal['weight']}, Height: {animal['height']}, Speed: {animal['speed']}"
                animals_info.append(animal_info)
            
            response_content = '\n'.join(animals_info)
            return HttpResponse(response_content)
        
        else:
            return HttpResponse("No animals found in this family.")
    else:
        return HttpResponse("Family not found.")