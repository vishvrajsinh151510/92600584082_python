# 7. Write a program to illustrate method resolution order and magic methods.
 
# resolution /Method Resolution Order (MRO)
class Student:
    def show(self):
         print("Student class")

class Teacher:
     def show(self):
          print("teacher class")

class Assistant(Student,Teacher):
     def __init__(self, name):
        self.name = name

     

a = Assistant("zala")
a.show()
print("MRO:",Assistant.mro())
print("Student Name:", a.name)


#megic method
print("--megic methods--")
class Abc:

     def __init__(self,name):
          self.name=name

     def __str__(self):
          return self.name
class Xyz:
     def __init__(self,value):
          self.value=value

     def __add__(self, other):
          return self.value+other.value
          

a=Abc("xyz")

print(a.name)
#str
print("str :",a)

n1=Xyz(20)
n2=Xyz(30)
print("add:",n1+n2)

