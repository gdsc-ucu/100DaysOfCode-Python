class Employee:
    def __init__(self, name, employee_id, salary):
        self.__name = name
        self.__employee_id = employee_id
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if self.validate_name(name):
            self.__name = name
        else:
            print("Invalid name format. Name should not be empty and must have the specific input.")

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def validate_name(self, name):
        if name.strip() and name.isalpha():
            return 1
        return 0
employee = Employee("Ezamati Ronald", "ERA1$42", 1000000000)

employee.set_name("Ezaston432")
print("Employee Name:", employee.get_name())

employee.set_name("Will Smik")
print("Employee Name:", employee.get_name())

print("Employee ID:", employee.get_employee_id())
print("Salary:", employee.get_salary())