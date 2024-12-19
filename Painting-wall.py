import math # We need to import the math module first, because we're gonna use the math.ceil
def painting(height, width): # Make a function first
    area_of_wall = height * width
    return area_of_wall  # So we return the area instead of printing it

height = int(input("Enter height of wall: "))
width = int(input("Enter width of wall: "))
coverage = 4

area = painting(height, width)
paint_needed = area / coverage  # Calculate paint needed
print(math.ceil(paint_needed))  # Use math.ceil to round up the result
