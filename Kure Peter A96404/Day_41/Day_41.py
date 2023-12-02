# Encapsulation
import math
class Shape:
    def __init__(self, *args):
        self.dimensions = args
    
    def getArea(self):
        raise NotImplementedError("Subclasses must implement getArea() method")

        
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
    def getArea(self):
        return math.pi * (self.dimensions[0]**2)
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def getArea(self):
        length, width = self.dimensions 
        return length * width

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)
    
    def getArea(self):
        base, height = self.dimensions
        return 0.5* base * height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def perimeter(self):
        return 4 * self.dimensions[0]
        
# Instances of the shapes
rectangle1 = Rectangle(17,10)
circle1 = Circle(9)
triangle1 = Triangle(12,16)
square = Square(5)

# Demontrating polymorphism
shapes = [("Rectangle",rectangle1),("Circle", circle1),("Triangle",triangle1),("Square",square)]

for shapeName, shape in shapes:
    if isinstance(shape, Square):
        print(f"{shapeName} has Area: {shape.getArea()} and Perimeter: {shape.perimeter()}")
    else:
        print(f"{shapeName} has Area: {shape.getArea()}")
