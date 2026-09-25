#Write a program to check whether a number is positive negative or zero
#using nested conditions.

num=int(input("Enetr the number:"))
if num>=0:
    if num==0:
        print("Zero")
    else:
        print("positive")
else:
    print("Nagative")
