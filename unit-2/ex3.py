#Write a program to generate a multiplication table using a for loop.

n=int(input("enter number"))

for i in range(1,11):
    print(n,'x',i,'=',(n*i))
