"""
@Author: DAShaikh
Logo: Windows 10 (https://www.microsoft.com/en-us/software-download/windows10)
"""

import turtle
import argparse


def draw(pen, i):
    """ Draw cuboid. """

    # Set pen color.
    pen.color(theme[theme_choice]["pen color"])

    # Initizalize cuboid fill color.
    pen.fillcolor(theme[theme_choice]["pen color"])
    pen.begin_fill()

    # Draw cuboid.
    pen.pendown()
    pen.goto(-50 - i, 50)
    pen.goto(65 - i, 65)
    pen.goto(65 - i, -65)
    pen.goto(-50 - i, -50)
    pen.goto(-50 - i, 0)

    # Fill the cuboid.
    pen.end_fill()

    # Configure the pen for drawing the '+'.
    pen.color(theme[theme_choice]["background"])

    # Draw the '+'.
    pen.goto(65 - i, 0)
    pen.penup()
    pen.goto(0 - i, 65)
    pen.pendown()
    pen.goto(0 - i, -65)


theme = {
            "white": {
                "background": "#0067b8",
                "pen color": "#ffffff"
                    },
            "blue": {
                "background": "#f1f3f2",
                "pen color": "#0079d2"
                    }
        }

# Read command-line arguments.
parser = argparse.ArgumentParser("Windows 10 logo animation.")
parser.add_argument("--theme", "-t", default="white", type=str,
                    help="Theme for Windows 10 logo. [white/blue]. DEFAULT='white'")

args = parser.parse_args()
theme_choice = args.theme.lower()

if theme_choice in theme:
    # Initialize the turtle pen and screen objects.
    pen = turtle.Turtle()
    screen = turtle.Screen()

    # Initialize background.
    screen.bgcolor(theme[theme_choice]["background"])

    # Initialize pen.
    pen.penup()
    pen.width(4)
    pen.speed("slowest")

    # Initialize start position.
    pen.setposition(-50, 0)

    # Draw the logo first time.
    draw(pen, 0)

    # Setup pen for animation.
    pen.speed(10)

    # Turn off tracer.
    screen.tracer(False)

    for i in range(10, 161, 10):
        # Clear the turtle work.
        pen.clear()

        # Redraw in a new position.
        draw(pen, i)

        # Update the screen.
        screen.update()

        # New position.
        pen.penup()
        pen.goto(-60 - i, -50)

    # Write "Windows 10".
    pen.penup()
    pen.goto(-65, -30)
    pen.color(theme[theme_choice]["pen color"])
    pen.write("Windows 10", font=("Segoe UI", 40))

    # Hide pen.
    pen.hideturtle()

    # Hold screen.
    screen.exitonclick()
else:
    print(f"Invalid theme choice: {theme_choice}")
