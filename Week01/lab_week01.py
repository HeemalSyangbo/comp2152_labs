# Sample Coding Questions 01 Week 01
# First Name: Heemal
# Last Name: Syangbo

# 1. Defining Variables: Array with elements 1, 4, 7, 9
array_variable = [1, 4, 7, 9]

# 2. Order of Operations
# Define variables a, b, c, d
a = 1
b = 2
c = 3
d = 4

# Fully-Bracketed Version of e = a * c - b / d
e1 = (a * c) - (b / d)

# Fully-Bracketed Version of e = a - b ** c // d + a % c
e2 = (a - ((b ** c) // d) + (a % c))

# 3. Formatting: Printing temperature with format
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

# 4. Common Functions: User input and age calculation
user_age = int(input("Enter your age: "))  # Get user input and convert to integer
user_age += 22  # Add 22 to the age
print(f"Now showing the shop items filtered by age: {user_age}")
