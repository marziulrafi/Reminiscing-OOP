"""
When a child class defines a method with the same name as one in the parent class,
the child's version overrides the parent's method.
"""



# Parent class
class Vehicle:
    def start(self):
        print("Starting the vehicle...")

# Child class overrides start()
class Car(Vehicle):
    def start(self):
        print("Starting the car engine...")

# Child class 2
class Bike(Vehicle):
    def start(self):
        print("Kick-starting the bike...")

# Create objects
v1 = Vehicle()
c1 = Car()
b1 = Bike()

v1.start()  # Parent method
c1.start()  # Child method overrides parent
b1.start()  # Another overridden method
