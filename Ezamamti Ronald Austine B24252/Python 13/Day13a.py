#import Day13
from Day13 import calculate_circle_area
def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"Area of the circle with radius {radius} is: {area:.2f}")
    except ValueError:
        print("Invalid radius, please do insert a positive radius.")
        
        
if __name__ == "__main__":
    main()