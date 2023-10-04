# functions
def multiply(): #defining the function name
    product=5*9*7*14*10 # multiplying the given numbers
    
    # printing the result
    print("The product is: ", product)
    
    # Printing an empty line for easier readability
    print()

def studentMarks(): #defining the function name
    names=["Peter", "Allan", "Joash"] #list of student names
    marks=[94,91,88] #list of marks
    
    # implementing the for loop to iterate through the names list
    for i in range(len(names)):
        
        # printing the names associated with their marks
        print(f"{names[i]}, your mark is {marks[i]}") 

# Calling the functions    
multiply()
studentMarks()