class NegativeValueError(Exception):
    def __init__(self, message="Value cannot be negative or zero"):
        self.message = message
        super().__init__(self.message)

def get_positive_number():
    try:
        num = int(input("Enter a positive number: "))
        if num < 1:
            raise NegativeValueError
        else:
            print("You entered positive value:", num)
    except NegativeValueError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        get_positive_number()

if __name__ == "__main__":
    get_positive_number()