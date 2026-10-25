#6. Write a program to demonstrate method overriding and polymorphism.

class Payment:
    def pay(self,amount):
         print("Processing payment:", amount)


class UPI:
     def pay(self,amount):
            print("Payment of Rs.", amount, "done using UPI")   

class CreditCard():
     def pay(self,amount):
          print("Payment of Rs.", amount, "done using Credit Card")

p1=UPI()
p1.pay(5000)

p2=CreditCard()
p2.pay(500)
