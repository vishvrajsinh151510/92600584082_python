
import re

text = "Python 123 is easy. Contact: student@gmail.com"

# Search for a word
result = re.search(r"Python", text)
if result:
    print("Word found:", result.group())

# Find all digits
numbers = re.findall(r"\d+", text)
print("Numbers found:", numbers)

# Find an email address
email = re.findall(r"\w+@\w+\.\w+", text)
print("Email found:", email)

# Check pattern at the beginning
result = re.match(r"Python", text)
if result:
    print("Text starts with:", result.group())
