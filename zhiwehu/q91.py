"""
Question:

Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.
"""


class Person:

    def __init__(self):
        pass

    def getGender(self):
        print "Unknown"


class Male(Person):

    def __init__(self):
        pass

    def getGender(self):
        print "Male"


class Female(Person):

    def __init__(self):
        pass

    def getGender(self):
        print "Female"


male = Male()
female = Female()
print male.getGender()
print female.getGender()
