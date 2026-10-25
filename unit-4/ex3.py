#  Write a program to illustrate instance variables and class variables.
class Student_data:

    # class variable
    school_name="Gyanpath School"
    graduation_clg="Darshan University"
    current_clg="Marwadi University"

    # instance variable
    def __init__(self,name,age,eno,clg_passing_year,cpi):
        self.name=name
        self.age=age
        self.eno=eno
        self.clg_passing_year=clg_passing_year
        self.cpi=cpi

    def display(self):
        print("\n----Student Details-----:")
        print(f" I am {self.name} and I am {self.age} years old. My enrollment number is {self.eno}. I have passed my graduation in {self.clg_passing_year} with a CPI of {self.cpi}. I have studied in {Student_data.school_name} and graduated from {Student_data.graduation_clg}. Currently, I am studying in {Student_data.current_clg}.")

def input_student_data():
    print("\n------Enter Student Data------:")
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    eno=int(input("Enter your enrollment number: "))
    clg_passing_year=int(input("Enter your graduation passing year: "))
    cpi=float(input("Enter your CPI: "))
    return name,age,eno,clg_passing_year,cpi

name,age,eno,clg_passing_year,cpi=input_student_data()
s1=Student_data(name,age,eno,clg_passing_year,cpi)
s1.display()

name,age,eno,clg_passing_year,cpi=input_student_data()
s2=Student_data(name,age,eno,clg_passing_year,cpi)
s2.display()




