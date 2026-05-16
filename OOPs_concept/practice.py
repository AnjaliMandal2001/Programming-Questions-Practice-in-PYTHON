from abc import ABC, abstractclassmethod

class Payment(ABC):
    @abstractclassmethod
    def pay(self,amount):
        pass

class UPI(Payment):
    def pay(self,amount):
        print(f"{amount} is paid by using")

class Card(Payment):
    def pay(self,amount):
        print(f"{amount} is paid by using")



obj1=Card()
obj1.pay(4500)