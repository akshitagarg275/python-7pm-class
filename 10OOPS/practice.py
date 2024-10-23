# Create a Car class with attributes like brand and model. Then create an instance of this class.
#  Add a method to the Car class that displays the full name of the car (brand and model).
# Add a static method to the Car class that returns a general description of a car
# Add a class variable to Car that keeps track of the number of cars created.

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

obj = Car('Tesla', 'Model S')
obj.carName()
print(obj.description())