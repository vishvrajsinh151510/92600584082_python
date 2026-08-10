#9.Write a program to explain mutable and immutable objects in Python

# Mutable 
a = [10, 20, 30]
print("Original List:", a)

a[0] = 100
print("After changing List:", a)


# Immutable Tuple
b = (10, 20, 30)
print("\nOriginal Tuple:", b)

# b[0] = 100      
print("Tuple cannot be changed because it is immutable")