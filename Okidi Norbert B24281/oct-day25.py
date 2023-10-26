import math

def compute_factorial():
    try:
        num = int(input("Enter a non-negative number to compute its factorial: "))
        if num < 0:
            raise ValueError("Input must be a non-negative integer.")
        factorial = math.factorial(num)
        return factorial
    except ValueError as e:
        print(f"Invalid input: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")

factorial_result = compute_factorial()
if factorial_result is not None:
    print(f"The factorial is: {factorial_result}")

