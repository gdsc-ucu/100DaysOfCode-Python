# Recursive function

import math

def factorial(x):
    if x == 1:
        return x
    else:
        return x*factorial(x-1)
    
num = int(input("Enter a number: "))

# 
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print(f"The factorial of {num} is {factorial(num)}")