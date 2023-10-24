# Write a Python program that asks the
# user to enter two numbers and
# calculates the result of dividing the
# first number by the second number.
# Handle errors when the user enters
# invalid input or tries to divide by zero.



try: 
    
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))

    result=num1/num2
    print("Result is :",result)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero!")

