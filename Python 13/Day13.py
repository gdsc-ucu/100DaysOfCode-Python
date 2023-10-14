import math
def calculate_circle_area(radius):
    if radius < 0:
        return "No negative radius allowed."
    else:
        return math.pi * radius**2
    