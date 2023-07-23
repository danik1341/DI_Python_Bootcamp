import math
import random

# EX XP

# 1)


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


def find_oldest_cat(cat_list: list[Cat]):
    oldest_cat = None
    max_age = 0

    if len(cat_list) == 0:
        return 'Mate your list is empty -_-'

    for cat in cat_list:
        if cat.age > max_age:
            oldest_cat = cat
            max_age = cat.age

    return oldest_cat


cat1 = Cat("Whiskers", 5)
cat2 = Cat("Mittens", 7)
cat3 = Cat("Jopa", 4)

cats = [cat1, cat2, cat3]

oldest_cat = find_oldest_cat(cats)

print(
    f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


print('/////////////////////////////////////////')


# 2)

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


davids_dog = Dog("Rex", 50)
print(
    f"David's dog: Name - {davids_dog.name}, Height - {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(
    f"Sarah's dog: Name - {sarahs_dog.name}, Height - {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is the bigger dog.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is the bigger dog.")
else:
    print("Both dogs are of the same height.")


print('/////////////////////////////////////////')


# 3)

class Song:
    def __init__(self, lyrics: list):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold",
                "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


print('/////////////////////////////////////////')


# 4)

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if (animal_sold in self.animals):
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animals = {}

        for animal in sorted(self.animals):
            letter = animal[0].upper()
            if letter in sorted_animals:
                sorted_animals[letter].append(animal)
            else:
                sorted_animals[letter] = [animal]

        return sorted_animals

    def get_groups(self):
        sorted_animals = self.sort_animals()
        print("Animals grouped by their first letter:")

        for group_num, animals_list in sorted_animals.items():
            if len(animals_list) == 1:
                print(f"{group_num}: '{animals_list[0]}'")
            else:
                print(f"{group_num}: {animals_list}")


ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Leopard")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Zebra")

ramat_gan_safari.get_animals()

print("Removing Giraffe from the zoo...")
ramat_gan_safari.sell_animal("Giraffe")

ramat_gan_safari.get_animals()

ramat_gan_safari.get_groups()

print('/////////////////////////////////////////')


# EX GOLD

# 1)

class Circle:
    def __init__(self, rad=1.0):
        self.rad = rad

    def perimeter(self):
        return 2 * math.pi * self.rad

    def area(self):
        return math.pi * self.rad ** 2

    def print_definition(self):
        print(
            f"A circle is a closed curve where all points are equidistant from the center point. It has a radius of {self.radius} units.")


circle1 = Circle()
circle2 = Circle(5.0)

print("Circle 1:")
print("Perimeter:", circle1.perimeter())
print("Area:", circle1.area())
circle1.print_definition()

print("\nCircle 2:")
print("Perimeter:", circle2.perimeter())
print("Area:", circle2.area())
circle2.print_definition()


print('/////////////////////////////////////////')

# 2)


class MyList:
    def __init__(self, letters):
        self.mylist = letters

    def reversed_list(self):
        return list(reversed(self.mylist))

    def sorted_list(self):
        return sorted(self.mylist)

    def random_numbers_list(self):
        return [random.randint(1, 100) for _ in range(len(self.mylist))]


letters = ['a', 'b', 'c', 'd', 'e']
my_list = MyList(letters)

print("Original List:", my_list.mylist)
print("Reversed List:", my_list.reversed_list())
print("Sorted List:", my_list.sorted_list())
print("Random Numbers List:", my_list.random_numbers_list())


print('/////////////////////////////////////////')


# 3)

class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True},
        ]

    def add_item(self, name, price, spice, gluten):
        new_dish = {'name': name, 'price': price,
                    'spice': spice, "gluten": gluten}
        self.menu.append(new_dish)
        print(f'{name} has been added to the menu')

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish['name'] == name:
                dish['price'] = price
                dish['spice'] = spice
                dish['gluten'] = gluten
                print(f"{name} has been updated in the menu.")
                return

        print(f'{name} is not in the menu.')

    def remove_item(self, name):
        for dish in self.menu:
            if dish['name'] == name:
                self.menu.remove(dish)
                print(f"{name} has been removed from the menu.")
                return

        print(f"{name} is not in the menu. Cannot remove.")


manager = MenuManager()
print("Current Menu:")
for dish in manager.menu:
    print(dish)

print("\nAdding new dish to the menu...")
manager.add_item("Pasta", 20, "A", False)

print("\nUpdating dish in the menu...")
manager.update_item("Soup", 12, "C", True)

print("\nRemoving dish from the menu...")
manager.remove_item("Hamburger")

print("\nUpdated Menu:")
for dish in manager.menu:
    print(dish)
