import math

def compute_factorial(n):
    if n < 0:
        return "Factorial is undefined for negative numbers."
    else:
        return math.factorial(n)

try:
    num = int(input("Enter a positive integer to compute its factorial: "))
    result = compute_factorial(num)
    print(f"{num}! = {result}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")