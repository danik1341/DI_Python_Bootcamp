# QUIZZ

# 1)

# A class is a blueprint or a template for creating objects in object-oriented programming (OOP).
# It defines a set of attributes (data) and methods (functions) that the objects of that class will have.


# 2)

# An instance is a specific occurrence or object created from a class.
# It represents a unique realization of the class,
# and each instance has its own set of attributes and values for those attributes.


# 3)

# Encapsulation is one of the four fundamental principles of object-oriented programming.
# It refers to the bundling of data (attributes) and methods (functions) that operate on that data within a single unit, which is the class.
# It helps in data hiding, protecting the internal details of a class from outside access.


# 4)

# Abstraction is another principle of object-oriented programming.
# It involves simplifying complex real-world objects by representing only the essential features and
# hiding unnecessary details. Abstraction allows us to create abstract classes and methods that provide a general structure without implementation details.


# 5)

# Inheritance is a concept in object-oriented programming where a class can inherit the attributes and methods of another class.
# The class that inherits from another class is called a subclass or derived class,
# and the class being inherited from is called the superclass or base class.
# It allows for code reuse and helps establish an "is-a" relationship.


# 6)

# Multiple inheritance occurs when a class inherits from more than one superclass.
# This means that a subclass can have attributes and methods from multiple base classes.
# It can lead to complex class hierarchies and potential conflicts if the same attribute or method is defined in multiple superclasses.


# 7)

# Polymorphism is the ability of a class or method to take on multiple forms.
# In object-oriented programming, it allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
# Polymorphism allows objects of different classes to be treated as objects of a common superclass, enabling more flexibility in code design.


# 8)

# Method Resolution Order (MRO) is the order in which Python looks for methods in a class hierarchy,
# especially in the case of multiple inheritance. Python uses the C3 linearization algorithm to determine the order in which it searches for a method when it is called on an object.
# The MRO ensures that the method is found following the inheritance chain, preventing method name conflicts and ensuring correct method execution.


import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Space"]
        self.values = ["A", "2", "3", "4", "5",
                       "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value)
                      for suit in self.suits for value in self.values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    for _ in range(5):
        card = deck.deal()
        if card:
            print(f"Dealing: {card}")
        else:
            print("Deck is empty.")
