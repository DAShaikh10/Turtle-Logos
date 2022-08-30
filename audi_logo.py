"""
@Author: DAShaikh
Logo: Audi (https://www.audi.com)
"""

import turtle
import argparse


theme = {
            "black": {
                "background": "#ffffff",
                "logo color": "#000000"
                    },
            "white": {
                "background": "#000000",
                "logo color": "#ffffff"
                    }
        }

# Read command-line arguments.
parser = argparse.ArgumentParser("Audi logo animation.")
parser.add_argument("--theme", "-t", default="black", type=str,
                    help="Theme for Audi logo. [black/white]. DEFAULT='black'")

args = parser.parse_args()
theme_choice = args.theme.lower()

if theme_choice in theme:
    # Initialize the turtle pen and screen objects.
    pen = turtle.Turtle()
    screen = turtle.Screen()

    # Set background color.
    screen.bgcolor(theme[theme_choice]["background"])

    # Set pen properties and initial position.
    pen.hideturtle()
    pen.speed("fast")
    pen.color(theme[theme_choice]["logo color"])

    # Draw the logo.
    for i in range(4):
        pen.penup()
        pen.goto(-100 + i * 70, -50)
        pen.pendown()
        pen.pensize(10)

        pen.circle(50)

    # Hold screen.
    screen.exitonclick()
else:
    print(f"Invalid theme choice: {theme_choice}")
