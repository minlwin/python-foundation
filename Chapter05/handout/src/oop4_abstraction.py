from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine starts 🚗")

class Bike(Vehicle):
    def start(self):
        print("Bike engine starts 🏍️")

# Using abstraction
vehicles = [Car(), Bike()]
for v in vehicles:
    v.start()
