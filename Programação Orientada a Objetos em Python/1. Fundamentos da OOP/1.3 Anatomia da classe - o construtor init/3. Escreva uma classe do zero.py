# Import the math module to use sqrt
import math

# Define the Point class
class Point:
    # Constructor with default values
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    # Method to calculate distance from origin (0, 0)
    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    # Method to reflect the point across x or y axis
    def reflect(self, axis):
        if axis == "x":
            self.y = -self.y
        elif axis == "y":
            self.x = -self.x
        else:
            print("Erro!")

# Test the class
pt = Point(x=3.0)
pt.reflect("y")          # Reflect across y-axis
print((pt.x, pt.y))      # Output: (-3.0, 0.0)

pt.y = 4.0               # Manually set y to 4.0
print(pt.distance_to_origin())  # Output: 5.0
