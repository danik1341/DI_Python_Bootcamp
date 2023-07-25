class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other_character):
        if not isinstance(other_character, Character):
            raise TypeError(
                "Parameter must be an instance of the Character class.")

        other_character.life -= self.attack
        print(f"{self.name} attacked {other_character.name}. {other_character.name}'s life reduced to {other_character.life}.")


class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Spirit of Elune guide {name}'s path")
        print("|----------------------------------------------------------------|")

    def meditate(self):
        self.life += 10
        self.attack -= 2
        print(f"{self.name} meditates, gaining Mark of The Wild buff, increasing life by 10 and decreasing attack by 2.")
        print("|----------------------------------------------------------------|")

    def animal_help(self):
        self.attack += 5
        print(
            f"Beasts of the forest heed {self.name} call! Attack increased by 5")
        print("|----------------------------------------------------------------|")

    def fight(self, other_character):
        damage = int(0.75 * self.life * self.attack)
        other_character.life -= damage
        print(f"{self.name} attacks {other_character.name} with nature's fury. {other_character.name}'s life reduced by {damage}.")
        print("|----------------------------------------------------------------|")


class Warrior(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(
            f"Mighty {self.name} entered the killing field. Lok'tar Ogar!!!!!!!")
        print("|----------------------------------------------------------------|")

    def brawl(self, other_character):
        damage = 2 * self.attack
        self.life += int(0.5 * self.attack)
        print(f"{self.name} engages in a brawl with {other_character.name}. "
              f"{self.name} bathes in his opponent's blood gaining {int(0.5 * self.attack)} life and {other_character.name} sufferes a devastating blow, reducing his life by {damage}.")
        print("|----------------------------------------------------------------|")

    def train(self):
        self.attack += 2
        self.life += 2
        print(f"{self.name} would not sit idle. Like a wet stone to a sword, {self.name} trains mind, body and soul, gaining 2 point to his attack and life")
        print("|----------------------------------------------------------------|")

    def roar(self, other_character):
        other_character.attack -= 3
        print(
            f"Lok'tar Ogar! {other_character.name} cowers in fear from {self.name} mighty roar, reducing his attack points by 3")
        print("|----------------------------------------------------------------|")


class Mage(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(
            f"The currents of magic are in upheaval. I, {self.name}, shall bend them to my will")
        print("|----------------------------------------------------------------|")

    def curse(self, other_character):
        other_character.attack -= 2
        print(
            f"Karabos kor koramond! {other_character.name} cursed by {self.name} vile magic, reducing his attack points by 2")
        print("|----------------------------------------------------------------|")

    def summon(self):
        self.attack += 3
        print(
            f"Chaos comes at my command! {self.name} summons a chaos minion increasing his attack by 3")
        print("|----------------------------------------------------------------|")

    def cast_spell(self, other_character):
        other_character.life -= self.attack/self.life
        print(f"{other_character.name} burns in arcane fire. {self.name} laugths as {other_character.name}'s flesh sizzling reducing their life by {self.attack/self.life}")
        print("|----------------------------------------------------------------|")


if __name__ == "__main__":
    druid = Druid("Forest Guardian")
    warrior = Warrior("Braveheart")
    mage = Mage("Wizardry")

    druid.meditate()
    druid.animal_help()
    druid.fight(warrior)

    warrior.brawl(druid)
    warrior.train()
    warrior.roar(mage)

    mage.curse(warrior)
    mage.summon()
    mage.cast_spell(druid)
