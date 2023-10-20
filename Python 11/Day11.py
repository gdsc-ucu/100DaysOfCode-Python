
def calculate_area_of_rectangle(length, width):
    if length <= 0 or width <= 0:
        return"invalid length or width"
    else:
        area = length * width
        return area
    
length = 4
width = 5
area = calculate_area_of_rectangle(length, width)
print("The area of the rectangle is:", area) 
        