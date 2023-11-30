


# Define a custom exception class
class NegativeValueError(Exception):
    pass

# Function to input a positive number
def number():
    number = int(input("Enter a positive number: "))
    if number < 0:
        raise NegativeValueError("Negative numbers are not allowed")
    return number

try:
    positive_number = number()
    print(f"You entered a positive number: {positive_number}")
except NegativeValueError as err:
    print(f"Error: {err}")

