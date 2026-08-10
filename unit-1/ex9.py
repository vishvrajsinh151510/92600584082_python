#9. Write a program to define and use user-defined functions with different types of arguments.

# No Argument, No Return
def  add():
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    print("addition:",a+b)

add()    

# Argument, No Return
# Positional Arguments
def sub(a,b):
     print("sub:",a-b)

sub(20,10)

# No Argument, Return
def multi():
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    return(a*b)

print("multi",multi())

# Argument, Return
def div(a,b):
    return a/b

print("div",div(20,5))



#  Keyword Arguments
def stu(name,age):
    print("Name:",name)
    print("age:",age)

stu(age=20,name="zala")

# Default Arguments

def student(name, course="MCA"):
    print("Name:", name)
    print("Course:", course)

student("zala")
student("zala", "BCA")

# Variable Length Arguments

def total(*n):
    sum=0
    for i in n:
        sum=sum+i
    print("total:",sum)
total(10,20)
total(10,20,5,5,5)