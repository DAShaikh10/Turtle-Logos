"""
@Author: DAShaikh
Logo: Mobil (https://www.mobil.com)
"""

import turtle


def draw_string(pen, pcolor, x, y, text):
    """ 
    Draw the input string. 
    
    Configurable methods: `color`, `goto`.
    """

    # Set properties and initial position.
    pen.color(pcolor)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    # Write text.
    pen.write(text, font=("Arial", 90, "bold"))


# Initialize the turtle pen and screen objects.
pen = turtle.Turtle()
screen = turtle.Screen()

# Hide pen.
pen.hideturtle()

# Write "Mobil".
draw_string(pen, "#0066b3", -150, -70, "M")
draw_string(pen, "#ed1b2f", -50, -70, "o")
draw_string(pen, "#0066b3", 20, -70, "bil")

# Hold screen.
screen.exitonclick()
