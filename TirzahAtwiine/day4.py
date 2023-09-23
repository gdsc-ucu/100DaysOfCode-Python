import math

#method 1
def Average_grade():

    name=input("Enter your name:")

    grade_1=int(input("Enter marks for assignment 1: "))
    grade_2=int(input("Enter marks for assignment 2: "))
    grade_3=int(input("Enter marks for assignment 2: "))

    average= (grade_1 + grade_2 + grade_3)/3
    print(f"{name},your average is {average}")

#method 2
def Average_grade2(grade_1,grade_2,grade_3):

    name=input("Enter your name:")

    average= round((grade_1 + grade_2 + grade_3)/3,2)
    print(f"{name},your average is {average}")

Average_grade()

Average_grade2(85,90,88)