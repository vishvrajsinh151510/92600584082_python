#Write a program to demonstrate list dictionary and set comprehensions.

# 1. LIST COMPREHENSION
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares_list = [x**2 for x in numbers if x % 2 == 0]

print("--- 1. List Comprehension ---")
print(f"Original numbers: {numbers}")
print(f"Squares of even numbers: {even_squares_list}\n")

 #2. DICTIONARY COMPREHENSION
words = ["apple", "banana", "cherry", "date"]
word_lengths_dict = {word: len(word) for word in words if len(word) > 4}

print("--- 2. Dictionary Comprehension ---")
print(f"Original words: {words}")
print(f"Words (>4 chars) mapped to lengths: {word_lengths_dict}\n")


# 3. SET COMPREHENSION
duplicated_numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]

unique_odds_set = {x for x in duplicated_numbers if x % 2 != 0}

print("--- 3. Set Comprehension ---")
print(f"Original list with duplicates: {duplicated_numbers}")
print(f"Unique odd numbers (Set): {unique_odds_set}\n")
