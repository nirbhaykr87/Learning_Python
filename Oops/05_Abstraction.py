from abc import ABC , abstractmethod

class Payment(ABC):

    @abstractmethod
    def security(self ):
        pass
 

class UPI(Payment):

    def show_balance(self , balance):
        print(f"Your bank account balance is {balance}")

    def security(self):
        print("securit check is OK")


obj1 = UPI()

obj1.show_balance("100")
obj1.security()