class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

my_point = Point3D(1, 2, 3)
print(my_point)

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

my_rectangle = Rectangle(width=3, length=4)
print(f"Area: {my_rectangle.area()}")
print(f"Perimeter: {my_rectangle.perimeter()}")

import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_inside(self, x, y):
        distance_squared = (x - self.center_x) ** 2 + (y - self.center_y) ** 2
        return distance_squared <= self.radius ** 2

# Create a new instance of Circle
my_circle = Circle(center_x=0, center_y=0, radius=5)
print(f"Area: {my_circle.area()}")
print(f"Perimeter: {my_circle.perimeter()}")
print(f"Is point (3, 4) inside the circle? {my_circle.is_inside(3, 4)}")
