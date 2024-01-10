#Write a program that takes user input
# for two numbers and performs division.
# Handle potential exceptions, such as
# division by zero, and provide
# appropriate error messages.

num1=int(input("Enter numerator: "))
num2=int(input("Enter denominator: "))

if num2==0:
    raise ZeroDivisionError ("Error! Number cannot be divisible by zero")
    

div=round(num1/num2,2)
print("Answer is: ",div)