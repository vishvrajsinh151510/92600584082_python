# Write a program to demonstrate recursion using factorial or Fibonacci series. 

#factorial

a=int(input("Enter the number"))
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print("factoral:",fact(a))

#fibonacci
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)

print("fibonacci:",fibo(a))
    