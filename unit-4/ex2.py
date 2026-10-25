# 2. Write a program to demonstrate constructor and destructor usage. 

class ATM:

    def __init__(self,name):
        self.name=name
        print("ATM session started for", self.name)

    def withdraw(self,amount):
        print(f"{self.name} withdraw your {amount} amount from ATM")

    def __del__(self):
        print("ATM session ended for", self.name)


c1=ATM("Zala")

c1.withdraw(1000)

print("Transaction completed")

del c1

print("Please visit again!")
