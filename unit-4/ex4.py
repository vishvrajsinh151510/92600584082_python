#4. Write a program to demonstrate instance methods class methods and static methods.

class Student:

    total_student=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.total_student+=1

    #instance
    def display(self):
        print(f"{self.name} is student and {self.age} year old")

    # class method
    @classmethod
    def count_student(cls):
        print("Total number of object created :",cls.total_student)
    
    @staticmethod
    def adult(age):
        if age>=18:
            print("student is adult!")
        else:
            print("Student is minor!")

s1=Student('zala',20)
s2=Student('jadeja',21)
s3=Student('xyz',25)

s1.display()

Student.adult(20)
# s1.adult(17)


Student.count_student()




