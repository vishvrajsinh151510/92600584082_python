# 4.Write a program to demonstrate string operations including slicing formatting and built-in string functions.
str=input("Enter string:")

print("\nOriginal String is:\n",str)

print("\nString Slicing\n")
#enter zala vishvrajsinh
print("First character:",str[0:1])
print(str[0:5])
print(str[5:13])
print(str[13:17])

print(str[5::2])
print(str[::2])
print(str[::-1])
print(str[2::-1])

print(str[-1::-1])

print(str[33:1:-1])

print(str[-2:-9:-1])
print(str[8:2:-2])
