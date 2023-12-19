class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = Student("Rocket", 25, "A")
student2 = Student("Steve", 21, "B")
student3 = Student("Ronald", 23, "A")

students = [student1, student2, student3]
total_age = sum(student.age for student in students)
average_age = total_age / len(students)

print("Average age for the students:", average_age)