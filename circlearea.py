# AREA OF A CIRCLE 
# area of a circle = 3.14 * radius * radius 

def circle_area(radius):
    area = 3.14 * radius * radius
    return area

radius = 5 

area = circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area}")

# When you place an f before a string, it allows you to embed variables and expressions inside the string by using curly braces {}

import math  # Import the math module to access the constant pi

def calculate_area_of_circle(radius):
    # Formula to calculate area: Area = π * r^2
    area = math.pi * radius ** 2  # math.pi provides the value of π
    return area  # Return the calculated area

# Example usage
radius = 5  # You can change the radius value here
area = calculate_area_of_circle(radius)
print(f"The area of the circle with radius {radius} is: {area}")

