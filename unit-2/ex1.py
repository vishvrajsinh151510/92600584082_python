#Write a program to demonstrate conditional statements using
#if if-else and if-elif-else.

#caluclater

while(True):
    a=float(input("Enter number:"))
    ch=input("Choose operator [+, -, *, /, %] or type '.' to EXIT:")
    if ch=='.':
        print("Exiting calculator. Goodbye!")
        break
    b=float(input("Enter 2number:"))
    if ch=='+':
          print(int(a+b))
    elif ch=='-':
        print(int(a-b))
    elif ch=='*':
        print(a*b)
    elif ch=='/':
        print(a/b)
    elif ch=='%':
        if b != 0:
            print(f"Result: {a % b}")
        else:
            print("Error: Cannot calculate remainder with zero.")
    else:
        print("INVALID Choice! Please try again")

    print("-" * 30) 
        



