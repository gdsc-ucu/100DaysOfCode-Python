import math
class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def calculate_perimeter(self):
        return 4 * self.length

rectangle = Rectangle(7, 6)
circle = Circle(4)
triangle = Triangle(4, 3)
square = Square(2)

# print("Rectangle Area:", rectangle.calculate_area())
# print("Circle Area:", circle.calculate_area())
# print("Triangle Area:", triangle.calculate_area())
print("Square Area:", square.calculate_area())
print("Square Perimeter:", square.calculate_perimeter())


# polymorphism
shapes = [rectangle, circle, triangle, square]

print("\nCalculate Areas using Polymorphism:")
for shape in shapes:
    print(f"{type(shape).__name__} Area:", shape.calculate_area())


print("\nSquare Perimeter:", square.calculate_perimeter())

