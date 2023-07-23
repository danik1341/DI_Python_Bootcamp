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
