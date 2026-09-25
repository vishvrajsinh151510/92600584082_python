#Write a program to generate a sequence of numbers using generator functions and yield keyword. 

def sequence(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1

print("--- Generating Sequence ---")
my_sequence = sequence(5)

for num in my_sequence:
    print(num)
