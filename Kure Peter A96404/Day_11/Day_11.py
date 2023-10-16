"""
Function to calculate area of a rectangle 
 when given length and width as parameters
"""
def Area():
    width=int(input("Enter the width: "))
    length=int(input("Enter the length: "))
    area = length*width
    print(f"Area of the rectangle is: {area} sq.units")
    
Area()