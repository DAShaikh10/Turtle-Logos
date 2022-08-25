"""
@Author: DAShaikh
Logo: FedEx (https://www.fedex.com)
"""

import turtle


def configure_pen(pen, pcolor, x, y):
    """ Set pen properties and position. """
    
    pen.color(pcolor)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


# Initialize the turtle pen and screen objects.
pen = turtle.Turtle()
screen = turtle.Screen()

# Hide pen.
pen.hideturtle()

# Set pen properties and initial position.
configure_pen(pen, "#4d148c", -205, -80)
pen.write("Fed", font=("Arial", 100, "bold"))

# Set new properties and position.
configure_pen(pen, "#ff6600", 12, -80)
pen.write("Ex", font=("Arial", 100, "bold"))

# Hold screen.
screen.exitonclick()
