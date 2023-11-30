class NegativeValueError(Exception):
    pass
    
def getPositiveNumber():
    print("Enter a positive number: ")
    number = int(input(">"))
    if number < 0:
        raise NegativeValueError("Negative numbers are not allowed!")
    return number
try:
    positiveNumber = getPositiveNumber()
    print(f"You have entered a positive number: {positiveNumber}")
except NegativeValueError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a number.")