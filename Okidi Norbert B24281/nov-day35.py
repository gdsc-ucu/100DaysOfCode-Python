class StudentGradingSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_name):
        self.students[student_name] = []

    def assign_grade(self, student_name, grade):
        if student_name in self.students:
            self.students[student_name].append(grade)
        else:
            print(f"Student {student_name} not found.")

    def calculate_average_grade(self, student_name):
        if student_name in self.students:
            grades = self.students[student_name]
            if grades:
                average = sum(grades) / len(grades)
                return average
            else:
                print(f"No grades assigned to {student_name}.")
        else:
            print(f"Student {student_name} not found.")

if __name__ == "__main__":
    grading_system = StudentGradingSystem()

    grading_system.add_student("Alice")
    grading_system.add_student("Bob")
    grading_system.add_student("Charlie")

    grading_system.assign_grade("Alice", 95)
    grading_system.assign_grade("Bob", 88)
    grading_system.assign_grade("Alice", 78)
    grading_system.assign_grade("Charlie", 90)
    grading_system.assign_grade("Charlie", 96)

    print("Average grade for Alice:", grading_system.calculate_average_grade("Alice"))
    print("Average grade for Bob:", grading_system.calculate_average_grade("Bob"))
    print("Average grade for Charlie:", grading_system.calculate_average_grade("Charlie"))

