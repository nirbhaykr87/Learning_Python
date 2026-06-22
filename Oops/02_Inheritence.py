class Car:
    def __init__(self , brand , price):
        self.__brand = brand    
        self.price = price

    def get_brand(self): 
        return f"{self.__brand}"
    
    def desc(self):
        return f"The car you have choose is {self.__brand}"


class Bike(Car):  # Here Bike is inheriting a class car
    def __init__(self, brand , price ,feul_capacity ):
        super().__init__(brand , price) 
        self.fuel_capacity= feul_capacity

    def desc(self):  # Here we are doing Method Overriding
        return f"The bike you have choose is {self.get_brand()}"
          # The reason for doing get_brand() is because Brand is a Private variable
          # and you cannot directly access that variable from child class , so to get access
          # of that variable we have already created a getter method to access that variable


    
bike1 = Bike("Honda" , "1 Lakh" , "15 Litre")
car1 = Car("BMW" , "50 Lakh" )

print(bike1.desc())
print(car1.desc())