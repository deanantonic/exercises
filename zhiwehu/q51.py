"""
Question:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
"""

from math import pi


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * pi


circle = Circle(10)
print circle.area()
