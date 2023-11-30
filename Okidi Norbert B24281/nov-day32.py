class Employee:
    def __init__(self, name, employee_id, salary):
        self.__name = self.__validate_name(name)
        self.__employee_id = employee_id
        self.__salary = salary

    def set_name(self, name):
        self.__name = self.__validate_name(name)

    def get_name(self):
        return self.__name

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def __validate_name(self, name):
        if len(name) >= 3:
            return name
        else:
            raise ValueError("Employee name must be at least 3 characters long")

employee = Employee("Okidi Norbert", 2015, 500000)


print("Employee Name:", employee.get_name())
print("Employee ID:", employee.get_employee_id())
print("Employee Salary:", employee.get_salary())

try:
    employee.set_name("A")
except ValueError as e:
    print("Error:", e)

employee.set_name("Apiyo Prossy")
print("Updated Employee Name:", employee.get_name())

