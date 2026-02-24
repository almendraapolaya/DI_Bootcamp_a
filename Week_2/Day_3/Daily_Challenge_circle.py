
# Daily Challenge - Circle

# #Instructions
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.

# Abilities of a Circle Instance
# Your Circle class should be able to:
# ✅ Compute the circle’s area.
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
# ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.

# Bonus Challenge (Optional)
# If you want an extra challenge:
# Install the Turtle module (pip install PythonTurtle)
# Draw the sorted circles visually on the screen!


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    
    def __repr__(self):
        return f"Circle(radius={self.radius:.2f})"

   
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return NotImplemented

    
    def __eq__(self, other):
        return self.radius == other.radius

    
    def __gt__(self, other):
        return self.radius > other.radius

    
    def __lt__(self, other):
        return self.radius < other.radius
    

import turtle

def draw_circles(circle_list):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    
    for c in circle_list:
        t.penup()
        
        t.goto(t.xcor() + (c.radius * 2) + 10, 0)
        t.pendown()
        t.circle(c.radius * 5) #
        
    screen.exitonclick()


# Create instances -
c1 = Circle(3)
c2 = Circle(5)

# 1. Diameter & Area -
print(f"C1 Diameter: {c1.diameter}") # Output: 6
print(f"C2 Area: {c2.area:.2f}")     # Output: 78.54

# 2. Addition - 
c3 = c1 + c2
print(f"New Circle from addition: {c3}") # Circle(radius=8.00)

# 3. Comparison -
print(f"Is C2 bigger than C1? {c2 > c1}") # True

# 4. Sorting -
circles = [Circle(10), Circle(2), Circle(7)]
circles.sort()
print(f"Sorted circles: {circles}") 
# Output: [Circle(radius=2.00), Circle(radius=7.00), Circle(radius=10.00)]


# Draw our sorted list
draw_circles(circles)