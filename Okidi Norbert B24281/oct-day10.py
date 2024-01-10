import calculator

number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))


sum = calculator.add(number1,number2)
product = calculator.multiply(number1,number2)
difference = calculator.substract(number1,number2)
division = calculator.divide(number1,number2)

print(f"Sum of {number1} and {number2} = {sum}")
print(f"Product of {number1} and {number2} = {product}")
print(f"Difference between {number1} and {number2} = {difference}")
print(f"Dividing {number1} by {number2} = {division}")