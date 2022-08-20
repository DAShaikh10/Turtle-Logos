"""
@Author: DAShaikh
Logo: Google Sheets (https://www.google.com/sheets)
"""

import turtle


def draw_rectangle(pen, x, y):
    """ 
    Draw rectangle.

    The co-ordinates `(x, y)` indicate the bottom right vertex of the rectangle.
    """

    # Set new pen position.
    pen.hideturtle()
    pen.penup()
    pen.goto(x, y)
    pen.setheading(180)
    pen.pendown()

    # Draw the rectangle.
    pen.forward(13)
    pen.right(90)
    pen.forward(8)
    pen.right(90)
    pen.forward(13)
    pen.right(90)
    pen.forward(8)


# Initialize the turtle pen and screen objects.
pen = turtle.Turtle()
screen = turtle.Screen()

# Set the initial position and pen color.
pen.hideturtle()
pen.penup()
pen.goto(-100, 5)
pen.color("#34a853")
pen.pendown()
pen.showturtle()

# Draw the outer rectangle.
pen.begin_fill()
pen.setheading(90)
pen.forward(30)
pen.circle(-2.5, 90)
pen.forward(30)
pen.right(45)
pen.forward(10)
pen.right(45)
pen.forward(45)
pen.circle(-2.5, 90)
pen.forward(35)
pen.circle(-2.5, 90)
pen.forward(50)
pen.end_fill()

# Hide pen.
pen.hideturtle()

# Draw the triangle.
pen.circle(-2.5, 90)
pen.forward(30)
pen.fillcolor("#188038")
pen.begin_fill()
pen.right(45)
pen.forward(13)
pen.right(135)
pen.forward(10)
pen.right(90)
pen.forward(8)
pen.right(135)
pen.end_fill()

# Set the new pen color and size.
pen.color("#ffffff")
pen.pensize(3)

# Draw the inner white rectangles.
draw_rectangle(pen, -80, 5)
draw_rectangle(pen, -80, -3)
draw_rectangle(pen, -67, -3)
draw_rectangle(pen, -67, 5)

# Set new position for writing "Google".
pen.penup()
pen.goto(-50, -10)
pen.color("#000000")
pen.pendown()

pen.write("Google", font=("Arial", 20, "bold"))

# Set new position for writing "Sheets".
pen.penup()
pen.goto(50, -10)
pen.color("#5f6368")
pen.pendown()

pen.write("Sheets", font=("Arial", 20))

# Hold screen.
screen.exitonclick()
