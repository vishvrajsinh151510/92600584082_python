# 8.Write a program to demonstrate encapsulation and abstraction using classes.

from abc import ABC, abstractmethod
#abstarction
class Bank(ABC):

    @abstractmethod
    def get_balance(self, entered_pin):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

#Encapsulation
class BankAcc:
    def __init__(self,owner,initial_balance,pin):
        self.owner=owner
        self.__balance=initial_balance
        self.__pin=pin

    def get_balance(self,enterd_pin):
        if enterd_pin==self.__pin:
            return f"your balnce:{self.__balance}"
        else:
            print("PIN wrong!")

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"{amount} successfully deposit")
        else:
            print("some error not deposit")


acc=BankAcc("zala",5000,1234)

print("ACCOUNT HOLDER:",acc.owner)

# print(acc.__balance)// error given
print(acc.get_balance(1234))
print(acc.get_balance(9999))

acc.deposit(2000)
print(acc.get_balance(1234))

