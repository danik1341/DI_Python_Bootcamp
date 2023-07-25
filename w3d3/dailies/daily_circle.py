import math
import turtle


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.diameter = diameter
        else:
            raise ValueError("Either radius or diameter must be provided.")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def draw(self):
        circle_drawing = turtle.Turtle()
        circle_drawing.circle(self.radius)
        return circle_drawing


c1 = Circle(radius=5)
c2 = Circle(diameter=10)

print(c1.radius)  # Output: 5
print(c2.diameter)  # Output: 10

print(c1.area)  # Output: 78.53981633974483
print(c2.area)  # Output: 78.53981633974483

print(c1)  # Output: Circle with radius: 5
print(repr(c2))  # Output: Circle(5.0)

c3 = c1 + c2
print(c3.radius)  # Output: 10.0

print(c1 < c3)  # Output: True
print(c1 <= c3)  # Output: True
print(c1 == c3)  # Output: False
print(c1 == c2)  # Output: True
print(c1 > c3)  # Output: False
print(c1 >= c3)  # Output: False

circle_list = [Circle(radius=3), Circle(radius=2), Circle(radius=5)]
circle_list.sort()
print(circle_list)  # Output: [Circle(2), Circle(3), Circle(5)]

c4 = Circle(radius=80)
c4.draw()
