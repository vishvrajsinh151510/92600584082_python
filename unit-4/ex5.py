# 5. Write a program to implement single multilevel and multiple inheritance

#single inherinace
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def show_product(self):
        print(f"product:{self.name}\nPrice:{self.price}")

class Electronics(Product):
        def __init__(self,name,price,warranty):
             super().__init__(name,price)
             self.warranty=warranty

        def show_details(self):
            #  super().show_product()
             self.show_product()
             print("Warranty:", self.warranty, "years")


#multilevel inheritance
class Leptop(Electronics):
     def __init__(self,name,price,warranty,ram,processor):
          super().__init__(name,price,warranty)
          self.ram=ram
          self.processor=processor

     def show_laopto(self):
           self.show_details()
           print("RAM:", self.ram, "GB")
           print("Processor:", self.processor)

#multiple 
class Warranty:
    def show_warranty_policy(self):
        print("Warranty policy: Repair or replacement")
    
class SmartPhone(Product,Warranty):
     def __init__(self, name, price,brand):
          super().__init__(name, price)
          self.brand=brand

     def show_phn(self):
          self.show_product()
          print("Brand:",self.brand)
          self.show_warranty_policy()
   

print("--Single Inheritance--")
p1=Electronics('Laptop',69999,2)
p1.show_details()


p2=Electronics("google",20,0)
p2.show_details()

#multilevel
print("\n--Multilevel Inheritance--")
l1=Leptop("Dell Laptop", 55000, 2, 16, "Intel i5")
l1.show_laopto()

print("\n--Multiple Inheritance--")
s1 = SmartPhone("Smartphone", 25000, "Samsung")
s1.show_phn()

        