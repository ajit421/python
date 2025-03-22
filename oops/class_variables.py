# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    number_of_cars = 0

    def __init__(self, brand, model):
        Car.number_of_cars += 1
        self.brand = brand
        self.model = model
        

    def get_number_of_cars(self):
        return Car.number_of_cars
    
my_car = Car("Tata", "Safari")

print(my_car.brand)
print(my_car.brand, my_car.model)
print(my_car.get_number_of_cars())
