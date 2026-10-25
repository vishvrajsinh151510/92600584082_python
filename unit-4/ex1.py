#1.  Write a program to create a class and object in Python

class Mca1b:
    subject="python"
    f_name="kP"

    def show(self,name):
        print("student name",name)


obj=Mca1b()
obj2=Mca1b()

print("Subject:", obj.subject)
print("Faculty Name:", obj.f_name)

#Mca1b.show(obj,"zala") 
obj.show("zala")
obj2.show("jadeja")


