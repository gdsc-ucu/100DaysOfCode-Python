import math

class Shape:
    def __init__(self, *args):
        self.dimensions = args

    def area(self):
        pass  

class Circle(Shape):
    def area(self):
        radius = self.dimensions[0]
        return 3.14 * radius * radius

class Rectangle(Shape):
    def area(self):
        length, width = self.dimensions
        return length * width

class Triangle(Shape):
    def area(self):
        base, height = self.dimensions
        return 0.5 * base * height


# polymorphism
rectangle = Rectangle(7, 6)
circle = Circle(4)
triangle = Triangle(4, 2)

shapes = [rectangle, circle, triangle]

for shape in shapes:
    print(f"Area of the shape: {shape.area()}")