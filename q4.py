# -*- coding: utf-8 -*-
import turtle
turtle.penup()
turtle.hideturtle()

# # Write a new class `Point` with these methods:
# # `__init__` sets `self.x` and `self.y`.
# # `__str__` returns "(x, y)" for your object's x- and y-coordinates.
# # `draw`:
# #    1. uses `turtle.goto` to go to that x and y coordinate
# #    2. stamps a point with `turtle.dot`



# # Make 4 new objects of the class Point: (0, 0), (100, 0), (100, 100), (0, 100)
# # Print your objects.
# # Run your draw method for that object.


# #### OPTIONAL extra credit ####
# # The `str` function will run the `__str__` method for an object. Use the
# # `turtle.write` method and the `str` function to add a label to your point
# # when you draw it.


# turtle.exitonclick()

# -*- coding: utf-8 -*-
import turtle

class Point:
    """A class to represent a point in 2D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        """Draw the point using turtle graphics."""
        turtle.goto(self.x, self.y)
        turtle.dot()
        turtle.write(f"({self.x}, {self.y})", align="center")


turtle.penup()
turtle.hideturtle()

# Create and draw points
points = [Point(0, 0), Point(100, 0), Point(100, 100), Point(0, 100)]
for point in points:
    point.draw()

turtle.exitonclick()