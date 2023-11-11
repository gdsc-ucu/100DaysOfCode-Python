import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        

    def area(self):
        return  self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length * self.width)

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
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(length = side, width = side)
    
    




rectangle = Rectangle(4,5)
circle = Circle(5)
triangle = Triangle(4, 9)
square = Square(4)

print(f"Area of a Rectangle: {rectangle.area()}")
print(f"Area of a Circle: {circle.area()}")
print(f"Area of a triangle: {triangle.area()}")
print(f"Area of a Square: {square.area()}")
print(f"Perimeter of a square: {square.perimeter()}")

shapes = [Rectangle(4,5), Circle(5), Triangle(4, 9), Square(4)]

for shape in shapes:
    print(f"Area: {shape.area()}")
    if isinstance(shape, Rectangle):
        print(f"Perimeter: {shape.perimeter()}")
