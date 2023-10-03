"""
A program to calculate the average grade
of a student named alice 
with grades 85,90 and 88 in her assignments
"""
# assigning Alice to the student_name variable
student_name = "Alice"

# creating a list of Alice's grades
grades=[85,90,88]

def gradeAverage(): #defining the function
    total=sum(grades) #calculating the sum of the grades
    
    #calculating the average grade
    avg=(total)/len(grades) 
    
    #Printing the name and average grade
    print(f"{student_name} has an average of {avg}")
    
# Calling the function
gradeAverage()