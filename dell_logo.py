"""
@Author: DAShaikh
Logo: Dell (https://www.dell.com)
"""

import turtle


def draw_L(pen):
    """ 
    Draw 'L'.  

    `pen color` and `initial position` must be set before calling this function.
    """

    pen.setheading(90)
    pen.pendown()
    pen.begin_fill()
    pen.forward(90)
    pen.right(90)
    pen.forward(20)
    pen.right(90)
    pen.forward(70)
    pen.left(90)
    pen.forward(40)
    pen.right(90)
    pen.forward(20)
    pen.right(90)
    pen.forward(60)
    pen.end_fill()


# Initialize the turtle pen and screen objects.
pen = turtle.Turtle()
screen = turtle.Screen()

# Set text color.
pen.color("#3287c1")

# Draw 'D' of the DELL logo.
pen.hideturtle()
pen.penup()
pen.goto(-130, -70)
pen.pendown()
pen.showturtle()

pen.begin_fill()
pen.setheading(90)
pen.forward(90)
pen.right(90)
pen.forward(50)
pen.circle(-46, 165)
pen.goto(-130, -70)
pen.speed("fastest")
pen.end_fill()

pen.penup()
pen.color("#ffffff")

pen.begin_fill()
pen.goto(-110, -50)
pen.pendown()
pen.setheading(90)
pen.forward(50)
pen.setheading(0)
pen.forward(30)
pen.circle(-25, 180)
pen.forward(30)
pen.end_fill()

# Draw 'E' of the DELL logo.
pen.speed("normal")
pen.color("#3287c1")
pen.penup()
pen.goto(-45,-15)
pen.pendown()
pen.setheading(0)
pen.left(35)
pen.begin_fill()
pen.forward(65)

for _ in range(2):
    pen.right(90)
    pen.forward(18)
    pen.right(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(50)

pen.right(90)
pen.forward(18)
pen.right(90)
pen.forward(65)
pen.right(85)
pen.forward(65)
pen.end_fill()

# Draw 'L' of the DELL logo.
pen.penup()
pen.goto(40, -70)
draw_L(pen)
pen.penup()
pen.goto(110, -70)
draw_L(pen)

# Draw circle.
pen.hideturtle()
pen.penup()
pen.goto(20, -200)
pen.pensize(15)
pen.pendown()
pen.showturtle()
pen.circle(-180)

# Hide pen.
pen.hideturtle()

# Hold screen.
screen.exitonclick()
