import math

class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
def calculate_total_area(Shapes):
    total_area = 0
    for shape in Shapes:
        total_area += shape.calculate_area()
    return total_area




Rectangle1 = Rectangle(6,6)
Rectangle2 = Rectangle(90,43)
Circle1 = Circle(45)
Circle2 = Circle(34)

shapes = [Rectangle1, Rectangle2, Circle1, Circle2]

total_area = calculate_total_area(shapes)

print(f"Total area of shapes: {total_area}")


        