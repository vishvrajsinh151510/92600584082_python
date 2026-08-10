# 3.Write a program to perform arithmetic relational and logical operations using Python operators.

#arithmetic operations
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))

print("\nArithmetic Operations\n")
print("Addition      :",n1+n2)
print("Subtraction   :",n1-n2)
print("Multiplication:",n1*n2)
print("Division      :",n1/n2)
print("Modulus       :",n1%n2)

print("\nRelational Operations\n")
print(f"number {n1} is Equal to {n2}       :",n1==n2)
print(f"number {n1} is Not Equal to {n2}   :",n1!=n2)
print(f"number {n1} is Greater than {n2}   :",n1>n2)
print(f"number {n1} is Less than {n2}      :",n1<n2)
print(f"number {n1} is Greater than or Equal to {n2}:",n1>=n2)
print(f"number {n1} is Less than or Equal to {n2}   :",n1<=n2)


print("\nLogical Operations\n")

if n1 > 0 and n2 > 0:
    print(f"Both {n1} and {n2} are positive numbers")
    print("this is and operation")

elif n1 > 0 or n2 < 0:
    print("one number is negative otherwise both are negative", n1, n2)
    print("this is or operation")

elif not(n1 < 0 and n2 > 0):
    print(f"Both {n1} and {n2} are not negative numbers")
    print("this is not operation")

else:
    print(f"Both {n1} and {n2} are negative numbers")



print("\nLogical Operations:")
print("(a > 0 and b > 0) :", n1 > 0 and n2 > 0)
print("(a > 0 or b > 0)  :", n1 > 0 or n2 > 0)
print("not(a > 0)        :", not(n1 > 0))