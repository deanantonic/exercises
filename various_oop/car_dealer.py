"""
Car Dealer

Create the following classes to make the tests run:

    Vehicle
    Truck
    Car

Vehicle

Place all the common properties into this "parent" object
Truck

Add extra carriage related functions - see the test and test results for more details
Car

Add the engine related (is_running, start_engine, stop_engine) parameter and functions to this class. Yes, a Truck should be also able to start it's engine, but it's not the main purpose now :)
"""


class Vehicle:

    ccm = 100
    top_speed = 500

    def __init__(self):
        pass


class Truck(Vehicle):

    carry_limit = 1000
    current_carriage_weight = None

    def __init__(self):
        pass

    def has_carriage(self):
        return True if self.current_carriage_weight else False

    def attach_carriage(self, carriage_weight):
        return True if carriage_weight <= Truck.carry_limit else False

    def detach_carriage(self):
        self.current_carriage_weight = None


class Car(Vehicle):

    is_running = False

    def __init__(self):
        pass

    def start_engine(self):
        Car.is_running = True

    def stop_engine(self):
        Car.is_running = False
