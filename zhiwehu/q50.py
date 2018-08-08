"""
Question:
Define a class named American and its subclass NewYorker.

Hints:

Use class Subclass(ParentClass) to define a subclass.
"""


class American:

    def __init__(self):
        pass

    def status(self):
        return "Active"


class NewYorker(American):
    pass

american = American()
newYorker = NewYorker()


print newYorker.status()
