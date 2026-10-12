# 1. Import the entire module
import math
print("Square root:", math.sqrt(25))

# 2. Import a specific function
from math import factorial
print("Factorial:", factorial(5))

# 3. Import with an alias
import math as m
print("Value of pi:", m.pi)

# 4. Import a specific function with an alias
from math import pow as power
print("Power:", power(2, 3))

# 5. Import all names from a module
from math import *
print("Ceiling:", ceil(4.3))
