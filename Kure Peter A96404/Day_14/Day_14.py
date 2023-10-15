def division():
    try:
        # Getting user input for the two numbers
        a= int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        
        # Performing the operation of divisions 
        result = a/b

    except ValueError:
        print("Error: Enter valid numbers!")

    except ZeroDivisionError:
        print('You cannot divide by zero')
    
    else:
        print(f"The result is: {result}")
        
# Calling the function
division()