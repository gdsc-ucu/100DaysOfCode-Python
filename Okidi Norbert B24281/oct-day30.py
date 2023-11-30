class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


studentObject1 = student("OKELLO PETTER", 20, "A")
studentObject2 = student("OPIYO SOLOMON", 19, "B")
studentObject3 = student("OCEN JOHNSON", 21, "A")

average_age = (studentObject1.age + studentObject2.age + studentObject3.age) / 3

print("STUDENT'S INFORMATION\n")
print(f"Student's Name: {studentObject1.name} Age: {studentObject1.age} Grade: {studentObject1.grade}\n")
print(f"Student's Name: {studentObject2.name} Age: {studentObject2.age} Grade: {studentObject2.grade}\n")
print(f"Student's Name: {studentObject3.name} Age: {studentObject3.age} Grade: {studentObject3.grade}\n")
print(f"Average age of Students: {average_age}")