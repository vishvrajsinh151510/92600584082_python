
import re

text = "Python is easy. Python version 3 is popular."

# Using match()
result = re.match(r"Python", text)
if result:
    print("Match:", result.group())

# Using search()
result = re.search(r"easy", text)
if result:
    print("Search:", result.group())

# Using findall()
result = re.findall(r"Python", text)
print("Findall:", result)
