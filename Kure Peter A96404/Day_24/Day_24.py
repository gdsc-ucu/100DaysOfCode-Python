# custom exception
class NegativeValueError(Exception):
    pass

# Function for user input
def getUserInput():
    number = float(input("Enter a positive number: "))
    if number < 0:
        raise NegativeValueError("Negative numbers are not allowed!")
    return number

# Main program
try:
    positiveNumber = getUserInput()
    print(f"You've entered a positive number: {positiveNumber}")
except ValueError:
    print("Invalid input. Please enter a number.")
except NegativeValueError as e:
    print(e)
