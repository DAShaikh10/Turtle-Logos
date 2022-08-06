"""
@Author: DAShaikh
"""

import turtle


# Initialize the pen and screen objects.
pen = turtle.Turtle()
screen = turtle.Screen()

# Set pen color.
pen.color("#F25022")

# Orange square.
pen.fillcolor("#F25022")
pen.begin_fill()
pen.penup()
pen.goto(-154, 4)
pen.pendown()
pen.goto(-204, 4)
pen.goto(-204, 50)
pen.goto(-154, 50)
pen.goto(-154, 4)
pen.end_fill()

# Set pen color.
pen.color("#7FBA00")

# Green square.
pen.fillcolor("#7FBA00")
pen.begin_fill()
pen.penup()
pen.goto(-150, 4)
pen.pendown()
pen.goto(-150, 50)
pen.goto(-100, 50)
pen.goto(-100, 4)
pen.goto(-150, 4)
pen.end_fill()

# Set pen color.
pen.color("#FFB900")

# Yellow square.
pen.fillcolor("#FFB900")
pen.begin_fill()
pen.penup()
pen.goto(-150, 0)
pen.pendown()
pen.goto(-100, 0)
pen.goto(-100, -50)
pen.goto(-150, -50)
pen.goto(-150, 0)
pen.end_fill()

# Set pen color.
pen.color("#00A4EF")

# Sky blue square.
pen.fillcolor("#00A4EF")
pen.begin_fill()
pen.penup()
pen.goto(-154, 0)
pen.pendown()
pen.goto(-204, 0)
pen.goto(-204, -50)
pen.goto(-154, -50)
pen.goto(-154, 0)
pen.end_fill()

# Set pen color.
pen.color("#000000")

# Write "Microsoft".
pen.penup()
pen.goto(-60, -30)
pen.color("#737373")
pen.write("Microsoft", font=("Segoe UI", 40, "bold"))

# Hide pen.
pen.hideturtle()

# Hold screen.
screen.exitonclick()
