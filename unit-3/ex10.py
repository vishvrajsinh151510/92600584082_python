
import re

# Create a text file
with open("data.txt", "w") as f:
    f.write("Name: Rahul\n")
    f.write("Email: rahul123@gmail.com\n")
    f.write("Phone: 9876543210\n")

# Read the text file
with open("data.txt", "r") as f:
    text = f.read()

# Extract email address
email = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

# Extract phone number
phone = re.findall(r'\b\d{10}\b', text)

print("Email:", email)
print("Phone:", phone)
