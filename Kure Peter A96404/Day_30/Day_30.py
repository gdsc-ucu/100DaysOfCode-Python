# Classes and objects
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
# Student objects
student1 = Student("Peter Drury", 24, "A")
student2 = Student("Alan Smith", 22, "A")

# Average age of the students
avAge = (student1.age + student2.age)/2
print(f"The average age of the students is {avAge}")