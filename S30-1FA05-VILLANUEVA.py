# Import the math module to use math functions like sqrt and pow
import math

# Get the x and y coordinates for both points from the user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the straight-line distance using the distance formula
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Print the final distance rounded to 2 decimal places
print(f"\nThe distance between the two points is: {distance:.2f}")
