"""
@Author: DAShaikh
Logo: Microsoft (https://www.microsoft.com)
"""

import turtle


# Initialize the turtle pen and screen objects.
pen = turtle.Turtle()
screen = turtle.Screen()

# Set initial position.
pen.hideturtle()
pen.penup()
pen.goto(-154, 4)
pen.pendown()
pen.showturtle()

# Set pen color to orange.
pen.color("#f25022")

# Draw the orange square.
pen.begin_fill()
pen.goto(-204, 4)
pen.goto(-204, 50)
pen.goto(-154, 50)
pen.goto(-154, 4)
pen.end_fill()

# Set pen color to green.
pen.color("#7fba00")

# Draw the green square.
pen.penup()
pen.goto(-150, 4)
pen.pendown()

pen.begin_fill()
pen.goto(-150, 50)
pen.goto(-100, 50)
pen.goto(-100, 4)
pen.goto(-150, 4)
pen.end_fill()

# Set pen color to yellow.
pen.color("#ffb900")

# Draw the yellow square.
pen.penup()
pen.goto(-150, 0)
pen.pendown()

pen.begin_fill()
pen.goto(-100, 0)
pen.goto(-100, -50)
pen.goto(-150, -50)
pen.goto(-150, 0)
pen.end_fill()

# Set pen color to sky blue.
pen.color("#00a4ef")

# Draw the sky blue square.
pen.penup()
pen.goto(-154, 0)
pen.pendown()

pen.begin_fill()
pen.goto(-204, 0)
pen.goto(-204, -50)
pen.goto(-154, -50)
pen.goto(-154, 0)
pen.end_fill()

# Hide pen.
pen.hideturtle()

# Set text color.
pen.color("#000000")

# Write "Microsoft".
pen.penup()
pen.goto(-60, -30)
pen.color("#737373")
pen.write("Microsoft", font=("Segoe UI", 40, "bold"))

# Hold screen.
screen.exitonclick()
