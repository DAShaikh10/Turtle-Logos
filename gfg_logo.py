"""
@Author: DAShaikh
Logo: GeeksforGeeks (https://www.geeksforgeeks.org)
"""

import turtle


# Initialize the turtle pen and screen objects.
pen = turtle.Turtle()
screen = turtle.Screen()

# Set pen color.
pen.pencolor("Green")

# Set pen properties.
pen.speed("fast")
pen.pensize(10)

# Set initial position.
pen.hideturtle()
pen.penup()
pen.goto(-160, 15)
pen.showturtle()
pen.pendown()

# Draw the horizontal line.
pen.setheading(180)
pen.forward(170)

# Draw the 'G' mirror image.
pen.setheading(-90)
pen.circle(40, 310)

# Set position back to the start of the horizontal line.
pen.hideturtle()
pen.penup()
pen.goto(-160, 15)
pen.pendown()
pen.showturtle()

# Draw the other 'G'.
pen.setheading(90)
pen.circle(40, -310)

# Hide pen.
pen.hideturtle()

# Write 'GeeksforGeeks'
pen.penup()
pen.goto(-130, -20)
pen.pendown()
pen.color("Black")
pen.write("GeeksforGeeks", font=("Consolas", 50, "bold"))

# Hold screen.
screen.exitonclick()
