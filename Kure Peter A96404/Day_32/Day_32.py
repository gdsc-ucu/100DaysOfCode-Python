class Employee:
    def __init__(self, name, employee_id, salary):
        self.__name = self.__validate_name(name)
        self.__employee_id = employee_id
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = self.__validate_name(name)

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def __validate_name(self, name):
        if not all(char.isalpha() or char.isspace() for char in name):
            raise ValueError("Name must contain only alphabetic characters.")
        return name

# Example usage:

# Create an Employee object
employee = Employee("John Cena", 75512, 50000)

# Access private attributes using methods
print(employee.get_name())  # Output: John Cena
print(employee.get_employee_id())  # Output: 75512
print(employee.get_salary())  # Output: 50000

# Set new values for attributes
employee.set_name("Mary Jane")
employee.set_employee_id(96587)
employee.set_salary(60000)

# Access private attributes again
print(employee.get_name())  # Output: Mary Jane
print(employee.get_employee_id())  # Output: 96587
print(employee.get_salary())  # Output: 60000

# Try to set an invalid name
try:
    employee.set_name(input("Enter a name: "))
    print(f"The name is valid")
except ValueError as e:
    print(e)  # Output if the name is not valid: Name must contain only alphabetic characters.
