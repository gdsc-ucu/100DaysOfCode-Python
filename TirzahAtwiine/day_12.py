

#create a function that finds the factorial of a number using recursion


def Factorial(num):
    
    if num==0:
        return 1   
    else:
        return num * Factorial(num-1)
    

#call the function
fac=Factorial(6)
print(fac)
        
