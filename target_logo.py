"""
@Author: DAShaikh
Logo: Target (https://corporate.target.com)
"""

import turtle
import argparse


theme = {
            "red": {
                "background": "#ffffff",
                "pen color": "#cc0001"
                    },
            "white": {
                "background": "#000000",
                "pen color": "#ffffff"
                    },
            "black": {
                "background": "#ffffff",
                "pen color": "#000000"
                    }
        }

# Read command-line arguments.
parser = argparse.ArgumentParser("Target logo animation.")
parser.add_argument("--theme", "-t", default="red", type=str,
                    help="Theme for Target logo. [red/white/black]. DEFAULT='red'")

args = parser.parse_args()
theme_choice = args.theme.lower()

if theme_choice in theme:
    # Initialize the turtle pen and screen objects.
    pen = turtle.Turtle()
    screen = turtle.Screen()

    # Initialize background.
    screen.bgcolor(theme[theme_choice]["background"])

    # Set pen properties.
    pen.hideturtle()
    pen.pensize(30)
    pen.color(theme[theme_choice]["pen color"])

    # Draw the inner circle.
    pen.circle(15)

    # Set new position.
    pen.penup()
    pen.goto(0, -65)
    pen.pendown()

    # Draw the outer circle.
    pen.circle(80)

    # Hold screen.
    screen.exitonclick()
else:
    print(f"Invalid theme choice: {theme_choice}")
