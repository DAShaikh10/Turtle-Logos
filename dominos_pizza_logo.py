"""
@Author: DAShaikh
Logo: Domino's pizza (https://pizzaonline.dominos.co.in)
"""

import turtle
import argparse


def draw_border(pen):
    """ 
    Draw the outer Domino's logo border. 
    
    Required for 'White' theme.
    """

    # Set initial position.
    pen.hideturtle()
    pen.penup()
    pen.goto(1, 45)
    pen.color("#ffffff")
    pen.pendown()
    pen.showturtle()

    # Draw the border.
    pen.begin_fill()
    pen.right(135)
    pen.forward(102)
    pen.circle(-5, 90)
    pen.forward(108)
    pen.circle(-5, 90)
    pen.forward(213)
    pen.circle(-5, 90)
    pen.forward(108)
    pen.circle(-5, 90)
    pen.forward(102)
    pen.end_fill()


# Read command-line arguments.
parser = argparse.ArgumentParser("Domino's Pizza logo animation.")
parser.add_argument("--theme", "-t", default="white", type=str,
                    help="Theme for Domino's Pizza logo. [white/blue]. DEFAULT='white'")

args = parser.parse_args()
theme_choice = args.theme.lower()

if theme_choice in ["white", "blue"]:
    # Initialize the turtle pen and screen objects.
    pen = turtle.Turtle()
    screen = turtle.Screen()

    # Initialize background.
    screen.bgcolor("#017eb4") if theme_choice == "white" else screen.bgcolor("#ffffff")
        
    if theme_choice == "white":
        draw_border(pen)

    # Set the initial position and pen color.
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 50)
    pen.color("#017eb4")
    pen.pendown()
    pen.setheading(0)
    pen.right(135)
    pen.showturtle()

    # Draw the blue square.
    pen.begin_fill()
    for _ in range(2):
        pen.forward(100)
        pen.circle(-5, 90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.end_fill()

    # Set new position for drawing the left inner circle. 
    pen.penup()
    pen.goto(-120, 40)
    pen.fillcolor("#ffffff")
    pen.pendown()

    # Draw the left inner circle.
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

    # Set new position for drawing the right inner circle.
    pen.penup()
    pen.goto(-60, 37)
    pen.pendown()

    # Draw the right inner circle.
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

    # Set new position for drawing the red square.
    pen.penup()
    pen.goto(-4, 61)
    pen.color("#e3163d")
    pen.pendown()

    # Draw the red sqaure.
    pen.begin_fill()
    pen.setheading(90)
    pen.right(-45)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.circle(-5, 90)
    pen.forward(100)
    pen.circle(-5, 90)
    pen.forward(100)
    pen.end_fill()

    # Set new position for drawing the inner circle.
    pen.penup()
    pen.goto(-10, 142)
    pen.pendown()

    # Draw the inner circle.
    pen.fillcolor("#ffffff")
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

    # Hide pen.
    pen.hideturtle()

    # Set text color.
    pen.color("#ffffff") if theme_choice == "white" else pen.color("#017eb4")

    # Set pen speed.
    pen.speed("fastest")

    # Set new position for writing "Domino".
    pen.penup()
    pen.goto(-170, -110)
    pen.pendown()

    pen.write("Domino", font=("Arial Rounded MT Bold", 60, "bold"))

    # Set new position for writing "'".
    pen.penup()
    pen.goto(120, -110)
    pen.pendown()

    pen.write("'", font=("Engravers MT", 60, "bold"))

    # Set new position for writing "s".
    pen.penup()
    pen.goto(140, -110)
    pen.pendown()

    pen.write("s", font=("Arial Rounded MT Bold", 60, "bold"))

    # Set new position for writing "Pizza".
    pen.penup()
    pen.goto(-100, -180)
    pen.pendown()

    pen.write("Pizza", font=("Arial Rounded MT Bold", 60, "bold"))

    # Hold screen.
    screen.exitonclick()
else:
    print(f"Invalid theme choice: {theme_choice}")
