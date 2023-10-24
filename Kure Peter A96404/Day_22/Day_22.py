# Errors and exceptions
print("Enter two numbers: ")
print("First number: ")
firstNumber = int(input(">"))
print("Second number: ")
secondNumber = int(input(">"))

# Handling the errors and exceptions
try:
    result = firstNumber/secondNumber
    print(f"The result is: {result}")
except ValueError:
    print("Invalid input! Enter valid numbers.")
except ZeroDivisionError as e:
    print(f"Error! Cant divide by zero.")
