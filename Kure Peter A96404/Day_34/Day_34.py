# Polymorphism

# Base Shape class
class Shape:
    def calculate_area(self):
        pass
    
# Rectangel subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
# Circle subclass 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        import math
        return math.pi * (self.radius**2)

# Function to calculate area of shapes in a list
def calcTotalArea(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.calculate_area()
    return total_area
# Usage
shapes = [Rectangle(9, 8), Circle(12)]
total_area = calcTotalArea(shapes)
print("Shapes and their values: Rectangle and Circle")
print("Rectangle -> length=9, width = 8")
print("Circle -> radius = 12")

# Printing the output of the area of the list of shapes
print(f"Total area of the shapes is : {total_area}")
