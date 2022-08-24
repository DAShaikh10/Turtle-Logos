"""
@Author: DAShaikh
Logo: CNN (https://edition.cnn.com)
"""

import turtle
import argparse


def configure_pen(pen, pcolor, psize, x, y):
    """ Set pen properties and position. """
    
    pen.color(pcolor)
    pen.pensize(psize)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def draw_ccn(pen, initial_step, last_step):
    """ Draw the CNN logo. """

    pen.setheading(180)
    pen.forward(initial_step)
    pen.circle(50, 180)
    pen.forward(50)
    pen.left(90)
    pen.forward(95)
    for _ in range(2):
        pen.circle(-5, 150)
        pen.forward(110)
        pen.circle(5, 180)
        pen.setheading(90)
        pen.forward(85)

    pen.forward(last_step)


theme = {
            "red": {
                "background": "#ffffff",
                "text color": "#cc0000"
                    },
            "white": {
                "background": "#cc0000",
                "text color": "#ffffff"
                    }
}

# Read command-line arguments.
parser = argparse.ArgumentParser("CNN logo animation.")
parser.add_argument("--theme", "-t", default="red", type=str,
                    help="Theme for CNN logo. [red/white]. DEFAULT='red'")

args = parser.parse_args()
theme_choice = args.theme.lower()

if theme_choice in theme:
    # Initialize the turtle pen and screen objects.
    pen = turtle.Turtle()
    screen = turtle.Screen()

    # Hide pen.
    pen.hideturtle()

    # Set properties and initial position.
    configure_pen(pen, theme[theme_choice]["text color"], 30, -55, 50)

    # Set background.
    screen.bgcolor(theme[theme_choice]["background"])

    # Draw the red outline.
    draw_ccn(pen, 15, 5)

    # Set new properties and position.
    configure_pen(pen, theme[theme_choice]["background"], 5, -41, 50)

    # Draw the inner white "CNN".
    draw_ccn(pen, 29, 20)

    # Hold screen.
    screen.exitonclick()
else:
    print(f"Invalid theme choice: {theme_choice}")
