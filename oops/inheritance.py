# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.


class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
class ElectricCar(Car):
    def __init__(self,country,battery_size,brand,model):
        self.country=country
        super().__init__(brand,model)
        self.battery_size=battery_size

my_tesla = ElectricCar("U.S", "85KWH", "Tesla", "model s")
print(my_tesla.battery_size)
print(my_tesla.model)
print(my_tesla.country)
