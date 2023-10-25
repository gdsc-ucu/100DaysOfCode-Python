class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative value encountered: {value}")

def get_postive_number():

    try:
        number = float(input("Enter any Positive numer: "))
        if number < 0:
            raise NegativeValueError(number)
        return number
    except ValueError:
        print("Invalid input: Please enter a vaild number.")
        return get_postive_number()
    except NegativeValueError as e:
        print(f"Error: {e.value} is a negative number. Please enter a positive number.")
        return get_postive_number()
    
try:
    postive_numer = get_postive_number()
    print(f"You have enter a positive number: {postive_numer}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
