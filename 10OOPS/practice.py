# Create a Car class with attributes like brand and model. Then create an instance of this class.
#  Add a method to the Car class that displays the full name of the car (brand and model).
# Add a static method to the Car class that returns a general description of a car
# Add a class variable to Car that keeps track of the number of cars created.
# Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
    
    def carName(self):
        print(f"{self.brand} - {self.model}")
    
    @staticmethod
    def description():
        return f"A car has 4 wheels."
    
    @classmethod
    def getInstanceCount(cls):
        return f"Number of instances : {cls.total_car}"
    
    def fuel_type(self):
        return "Car fuel type"

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def fuel_type(self):
       print("It is working on the batteries")

obj = Car('Tesla', 'Model S')
# obj.carName()
# print(obj.description())

print(Car.getInstanceCount())