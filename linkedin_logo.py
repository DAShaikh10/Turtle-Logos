"""
@Author: DAShaikh
Logo: Linkedin (https://www.linkedin.com)
"""

import turtle
import argparse


def draw_linkedin(pen, txt_color, box_color, in_color):
    """ Draw the LinkedIn logo. """
    
    # Set initial position.
    pen.hideturtle()
    pen.penup()
    pen.goto(-250, -50)
    pen.pendown()

    # Set text color and write "Linked".
    pen.color(txt_color)
    pen.write("Linked", font=("Segoe UI", 80, "bold"))

    # Set new position for drawing the square.
    pen.penup()
    pen.goto(110, -40)
    pen.pendown()
    pen.showturtle()

    # Set pen color for drawing the square.
    pen.color(box_color)

    # Draw the square and fill it.
    pen.begin_fill()
    for _ in range(4):
        pen.forward(100)
        pen.circle(10, 90)
    pen.end_fill()

    # Set new position for writing "in".
    pen.penup()
    pen.hideturtle()
    pen.goto(115, -45)
    pen.showturtle()
    pen.pendown()

    # Set text color and write "in".
    pen.color(in_color)
    pen.write("in", font=("Segoe UI", 80, "bold"))

    # Hide pen.
    pen.hideturtle()


theme = {
            "2-color": {
                "background": "#f1f2f4",
                "text color": "#000000",
                "box color": "#0077b6",
                "in color": "#fffeff"
                    },
            "2-color-reversed": {
                "background": "#1f2022",
                "text color": "#ffffff",
                "box color": "#0076b5",
                "in color": "#fffefc"
                    },
            "black": {
                "background": "#d0edfb",
                "text color": "#020005",
                "box color": "#000200",
                "in color": "#d3edfb"
                    },
            "reversed-white": {
                "background": "#0077b4",
                "text color": "#fffdff",
                "box color": "#fffdff",
                "in color": "#0077b4"
                    },
        }

# Read command-line arguments.
parser = argparse.ArgumentParser("LinkedIn logo animation.")
parser.add_argument("--theme", "-t", default="2-color", type=str,
                    help="Theme for LinkedIn logo. [2-color/2-color-reversed/black/reversed-white]. DEFAULT='2-color'")

args = parser.parse_args()
theme_choice = args.theme.lower()

if theme_choice in theme:
    # Initialize the turtle pen and screen objects.
    pen = turtle.Turtle()
    screen = turtle.Screen()

    # Set background color.
    screen.bgcolor(theme[theme_choice]["background"])
    
    # Draw logo.
    draw_linkedin(pen, theme[theme_choice]["text color"], theme[theme_choice]["box color"], theme[theme_choice]["in color"])

    # Hold screen.
    screen.exitonclick()
else:
    print(f"Invalid theme choice: {theme_choice}")
