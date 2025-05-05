class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        #self.total_car
        Car.total_car += 1

    def get_brand(self):
        return self.__brand+"!"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_des():
        return "carsv aee"
    
    @property
    def model(self):
        return self.__model
    
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric charge"
    
    

my_tesla=ElectricCar("Tesla","Model S","85kWh")
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))
#print(my_tesla.__brand)
print(my_tesla.full_name())
print(my_tesla.get_brand())
print(my_tesla.fuel_type())
print(ElectricCar.general_des())
print(my_tesla.general_des())


my_car = Car("tot","coro")
#print(my_car.brand)
#print(my_car.model)
print(my_car.full_name())
print(my_car.fuel_type())
print(Car.general_des())
print(my_car.general_des())
#my_car.model = "city"
print(my_car.model)
#print(my_car.model())

my_new_car=Car("tata","safari")
print(my_new_car.model)
print(my_new_car.get_brand())
print(my_new_car.fuel_type())
print(Car.total_car)

class battery:
    def battery_info(self):
        return "this is battery"

class engine:
    def engine_info(self):
        return "this is engine"

class electriccartwo(battery,engine,Car):
    pass


my_new_tesla = electriccartwo("tesla1","model2")

print(my_new_tesla.engine_info())
print(my_new_tesla.get_brand())
print(my_new_tesla.model) 
print(my_new_tesla.battery_info())