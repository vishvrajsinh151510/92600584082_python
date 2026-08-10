# 2.Write a program to illustrate the use of different data types and type casting. 

n = int(input("Enter an integer value:"))
f = float(input("Enter a floating-point value:"))
text = input("Enter a string value:")
bol=bool(input("Enter a boolean value (True/False):"))

print("type of n:",n, type(n))
print("type of f:",f, type(f))
print("type of text:",text, type(text))
print("type of bol:",bol, type(bol))


print("\nAfter type casting:")
print("Integer to float:", float(n))
print("Float to integer:", int(f))
print("Integer to String:", str(n))
print("Boolean to integer:", int(bol))
