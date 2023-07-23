class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal: str, num=1):
        if animal in self.animals:
            self.animals[animal] += num
        else:
            self.animals[animal] = num

    def get_info(self):
        farm_info = f"{self.name}'s farm\n\n"

        for animal, num in self.animals.items():
            farm_info += f"{animal} : {num}\n"

        farm_info += "\nE-I-E-I-0!"
        return farm_info

    def get_animal_types(self):
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_str = ', '.join(animal_types)
        return f"{self.name}'s farm has {animal_str}."


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
