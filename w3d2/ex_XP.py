import random


# EX XP

# 1)


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


bengal_cat = Bengal("Bengal Cat", 3)
chartreux_cat = Chartreux("Chartreux Cat", 2)
siamese_cat = Siamese("Siamese Cat", 4)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]
sara_pets = Pets(all_cats)

sara_pets.walk()


print('/////////////////////////////////////////')


# 2)

class Dog():
    def __init__(self, name: str, age: int, weight: int):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age*10

    def fight(self, other_dog):  # We went a bit dark with this one, aint we?
        my_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight

        if my_score > other_score:
            return f"{self.name} won the fight"
        elif my_score < other_score:
            return f"{other_dog.name} won the fight"
        else:
            return "It's a tie"


dog1 = Dog("Buddy", 5, 15)
dog2 = Dog("Rocky", 4, 12)
dog3 = Dog("Max", 3, 10)

print(dog1.bark())
print(f"{dog1.name}'s running speed: {dog1.run_speed()}")

print(dog2.bark())
print(f"{dog2.name}'s running speed: {dog2.run_speed()}")

print(dog3.bark())
print(f"{dog3.name}'s running speed: {dog3.run_speed()}")

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))


print('/////////////////////////////////////////')

# 2)

# I wont create a new file but if I would import the Dog class like so -

# from __FILE NAME__ import Dog ................ Again for the sake of the teachers I wont created another file <3


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        super().bark()
        self.trained = True

    def play(self, *other_dogs):
        print(f"{self.name} and {', '.join(other_dogs)} all play together")

    def do_a_trick(self):
        if self.trained:
            trick_options = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(trick_options))


dog1 = PetDog("Buddy", 5, 15)
dog2 = PetDog("Rocky", 4, 12)
dog3 = PetDog("Rex", 3, 14)

dog1.train()
dog1.play(dog2.name, dog3.name)
dog1.do_a_trick()
