"""
Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
"""


class Foo:

    color = "green"

    def __init__(self, color=None):
        self.color = color


bar = Foo()

print Foo.color
print bar.color

Foo.color = "orange"
bar.color = "red"
print Foo.color
print bar.color
