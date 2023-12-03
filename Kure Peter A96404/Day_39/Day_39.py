# Polymorphism
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
    
# Instances of the shapes
rectangle1 = Rectangle(17,10)
circle1 = Circle(9)

# Areas
area=rectangle1.getArea()
area1 = circle1.getArea()

# Printing the areas of the shapes
print(f"The area of the rectangle is {area} sq.units")
print(f"The area of the circle is {area1} sq.units")