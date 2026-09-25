#. Write a program to demonstrate iterators and iterables in Python. 
fruits = ["Apple", "Banana", "Cherry"]
fruit_iterator = iter(fruits)

print("--- Manual Traversal ---")
print(next(fruit_iterator))
print(next(fruit_iterator))
print(next(fruit_iterator))


def countdown_generator(start):
    while start > 0:
        yield start
        start -= 1

print("\n--- Generator Iteration via for-loop ---")
counter_iterator = countdown_generator(3)

for num in counter_iterator:
    print(num)
