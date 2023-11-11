import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height




rectangle = Rectangle(4,5)
circle = Circle(5)
triangle = Triangle(4, 9)

print(f"Area of a Rectangle: {rectangle.area()}")
print(f"Area of a Circle: {circle.area()}")
print(f"Area of a triangle: {triangle.area()}")

shapes = [Rectangle(4,5), Circle(5), Triangle(4, 9)]

for shape in shapes:
    print(f"Area: {shape.area()}")
