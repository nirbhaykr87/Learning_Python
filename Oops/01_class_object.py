class Car:
    def __init__(self , brand , price):
        self.__brand = brand    # __ represents a Private variables
        self.price = price

    def get_brand(self):
        return f"The brand of the car is {self.__brand}"


car1=Car("Toyoto" , "50 Lakhs") # Car1 is a object 
# car1.brand = "Honda"  ------> Here you are creating a new attributes called as brand
# print(car1.brand) -- Gives you 'Honda '
print(car1.get_brand())