"""
A program to calculate the average grade
of a student named Alice 
with grades 85,90 and 88 in her three assignments
"""
# assigning Alice to the student_name variable
student_name = "Alice"

# A list of Alice's grades
grades=[85,90,88]

def gradeAverage(): #defining the function
    total=sum(grades) #calculating the sum of the grades
    
    #calculating the average grade
    avg=(total)/len(grades) 
    
    #Printing the student name and average grade
    print(f"{student_name} has an average of {avg} in her assignments")
    
# Calling the function
gradeAverage()