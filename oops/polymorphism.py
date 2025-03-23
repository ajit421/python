# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def fuel_type(self):
        return "Gasoline or Diesel"

class ElectricCar(Car):
    def fuel_type(self):
        return "Electricty"
    
car = Car()
electric_car =  ElectricCar()

print("Car fuel type: ", car.fuel_type())
print("Electric Car fuel type: ", electric_car.fuel_type())
