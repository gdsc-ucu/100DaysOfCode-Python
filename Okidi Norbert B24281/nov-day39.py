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




rectangle = Rectangle(4,5)
circle = Circle(5)

print(f"Area of a Rectangle: {rectangle.area()}")
print(f"Area of a Circle: {circle.area()}")







        