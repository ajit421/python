# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

# from oops.inheritance import ElectricCar

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    
    def get_brand(self):
        return self.__brand +"!"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    
my_tesla = ElectricCar ("Tesla", "model m", '85KWH')
print(my_tesla.get_brand())
        