import math
class NegativeValueError(Exception):
    pass

def factorial(n):
    if n < 0:
        raise NegativeValueError("Factorial is not defined for negative numbers")
    else:
        return math.factorial(n)

try:
    num = int(input("Enter an integer: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
except NegativeValueError as e:
    print(e)
except ValueError:
    print("Invalid input, please enter a number.")
