#Write a program to find the sum of digits of a number using a while loop.

a=int(input("Enter number:"))
n=a
sum=0
while(n!=0):
    l=n%10
    sum=sum+l
    n=n//10
    
print(sum)
    
    
user_input=input("Enter digit separat by space: ")

digit_list=user_input.split()
add=0
for digit in digit_list:
    add=add+int(digit)
    
print(add)
    
