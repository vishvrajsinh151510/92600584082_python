#Write a program to iterate over lists strings and dictionaries using loops. 

# 1. ITERATING OVER A LIST
print("--- Iterating over a List ---")
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"Fruit: {fruit}")
    
    
    
# 2. ITERATING OVER A STRING
print("\n--- Iterating over a String ---")
word = "Python"
for letter in word:
    print(f"Letter: {letter}")
    

# 3. ITERATING OVER A DICTIONARY
print("\n--- Iterating over a Dictionary ---")
user_profile = {
    "username": "coder123",
    "role": "developer",
    "status": "active"
}

print("Option A (Keys and Values):")
for key, value in user_profile.items():
    print(f"  {key}: {value}") 
    

print("\nOption B (Keys only):")
for key in user_profile:
    print(f"  Key: {key}")
    
print("\nOption C (Values only):")
for value in user_profile.values():
    print(f"  Value: {value}")