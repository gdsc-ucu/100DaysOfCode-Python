try:
    first_number = float(input("Enter your first number: "))
    second_number = float(input("Enter your second number: "))

    result = first_number / second_number
    print(result)
except ZeroDivisionError:
    print("Can not divide by zero")
