# calculator sytem using method overloading

from multipledispatch import dispatch

# Addition
@dispatch(int, int)
def add(a, b):
    return a + b

@dispatch(float, float)
def add(a, b):
    return a + b

@dispatch(str, str)
def add(a, b):
    return a + b

# Subtraction
@dispatch(int, int)
def subtract(a, b):
    return a - b

@dispatch(float, float)
def subtract(a, b):
    return a - b

# Multiplication
@dispatch(int, int)
def multiply(a, b):
    return a * b

@dispatch(float, float)
def multiply(a, b):
    return a * b

# Division
@dispatch(int, int)
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

@dispatch(float, float)
def divide(a, b):
    if b == 0.0:
        return "Error: Division by zero"
    return a / b

# Power
@dispatch(int, int)
def power(a, b):
    return a ** b

@dispatch(float, float)
def power(a, b):
    return a ** b

# Concatenation for multiple strings
@dispatch(str, str, str)
def add(a, b, c):
    return a + b + c

# Summing three numbers
@dispatch(int, int, int)
def add(a, b, c):
    return a + b + c

@dispatch(float, float, float)
def add(a, b, c):
    return a + b + c

# Addition using different data types
print("Addition (int):", add(5, 3))
print("Addition (float):", add(2.5, 4.1))
print("Addition (str):", add("Hello, ", "World!"))
print("Addition (3 ints):", add(1, 2, 3))
print("Addition (3 floats):", add(1.1, 2.2, 3.3))
print("Addition (3 strings):", add("Python ", "is ", "fun!"))

# Subrtration using different data types
print("Subtraction (int):", subtract(10, 4))
print("Subtraction (float):", subtract(10.5, 2.5))

# Multiplication using different data types
print("Multiplication (int):", multiply(6, 7))
print("Multiplication (float):", multiply(1.5, 4.0))

# Division using different data types
print("Division (int):", divide(20, 5))
print("Division (float):", divide(7.5, 2.5))
print("Division by zero:", divide(5, 0))

# Power using different data types
print("Power (int):", power(2, 3))
print("Power (float):", power(2.5, 2.0))

#output
# Addition (int): 8
# Addition (float): 6.6
# Addition (str): Hello, World!
# Addition (3 ints): 6
# Addition (3 floats): 6.6
# Addition (3 strings): Python is fun!
# Subtraction (int): 6
# Subtraction (float): 8.0
# Multiplication (int): 42
# Multiplication (float): 6.0
# Division (int): 4.0
# Division (float): 3.0
# Division by zero: Error: Division by zero
# Power (int): 8
# Power (float): 6.25

# [Done] exited with code=0 in 0.168 seconds
