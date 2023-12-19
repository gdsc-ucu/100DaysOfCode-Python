try:
    number1 = float(input("Enter the first number:"))
    number2 = float(input("Enter the second number:"))
    
    division = number1/number2
    print(f"{number1} / {number2} = {division}") 
    
except ZeroDivisionError:
    print("Can not divide by zero!")
    
