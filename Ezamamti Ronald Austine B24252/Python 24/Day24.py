class NegativeValueError(Exception):
    def __init__(self, message="Negative values are not allowed"):
        self.message = message
        super().__init__(self.message)

def main():
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise NegativeValueError
        else:
            print("You entered a valid number:", num)
    except NegativeValueError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        main()

if __name__ == "__main__":
    main()