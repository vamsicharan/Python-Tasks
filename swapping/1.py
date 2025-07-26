# Swap two numbers without using a third variable

# Input from user
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print(f"Before swapping: a = {a}, b = {b}")

# Swapping using arithmetic operations
a = a + b
b = a - b
a = a - b

# Output result
print(f"After swapping: a = {a}, b = {b}")
