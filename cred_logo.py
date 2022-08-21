"""
@Author: DAShaikh
Logo: Cred (https://cred.club)
"""

import turtle
import argparse


def draw_cred(pen, logo_color):
    """ Draw the CRED logo. """

    # Set properties and initial position.
    pen.hideturtle()
    pen.penup()
    pen.goto(-125, 170)
    pen.pensize(20)
    pen.color(logo_color)
    pen.pendown()
    pen.showturtle()

    # Draw the outer pentagon.
    pen.forward(250)
    pen.right(90)
    pen.forward(200)
    pen.right(60)
    for _ in range(2):
        pen.forward(150)
        pen.right(60)
    pen.forward(200)
    pen.right(90)
    pen.forward(5)

    # Draw the inner top and right side.
    pen.penup()
    pen.goto(-50, 120)
    pen.pendown()

    pen.forward(120)
    pen.right(90)
    pen.forward(50)
    pen.penup()
    pen.forward(40)
    pen.pendown()
    pen.forward(35)
    pen.right(60)

    # Draw the bottom.
    for _ in range(2):
        pen.forward(90)
        pen.right(60)
    pen.forward(80)
    pen.right(90)
    pen.forward(100)

    # Draw the inner most shape.
    pen.penup()
    pen.goto(20, 15)
    pen.pendown()

    pen.right(150)
    pen.forward(35)
    pen.right(60)
    pen.forward(35)
    pen.right(60)
    pen.forward(20)

    # Hide pen.
    pen.hideturtle()

    # Set new position for writing "CRED".
    pen.penup()
    pen.goto(-130, -220)
    pen.pendown()

    pen.write("CRED", font=("Arial", 65))


theme = {
            "white": {
                "background": "#000000",
                "logo color": "#ffffff"
                    },
            "black": {
                "background": "#ffffff",
                "logo color": "#000000"
                    },
        }

# Read command-line arguments.
parser = argparse.ArgumentParser("CRED logo animation.")
parser.add_argument("--theme", "-t", default="white", type=str,
                    help="Theme for CRED logo. [white/black]. DEFAULT='white'")

args = parser.parse_args()
theme_choice = args.theme.lower()

if theme_choice in theme:
    # Initialize the turtle pen and screen objects.
    pen = turtle.Turtle()
    screen = turtle.Screen()
    
    # Set background color.
    screen.bgcolor(theme[theme_choice]["background"])

    # Draw logo.
    draw_cred(pen, theme[theme_choice]["logo color"])

    # Hold screen.
    screen.exitonclick()
else:
    print(f"Invalid theme choice: {theme_choice}")
