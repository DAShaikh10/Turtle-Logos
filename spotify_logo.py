"""
@Author: DAShaikh
Logo: Spotify (https://www.spotify.com)
"""

import turtle
import argparse


def draw_spotify(pen, bgcolor, circle_color):
    """ Draw the Spotify logo. """

    # Set properties and initial position.
    pen.hideturtle()
    pen.speed("fast")
    pen.penup()
    pen.goto(-160, -90)
    pen.pendown()
    pen.showturtle()

    # Draw the circle.
    pen.color(circle_color)
    pen.begin_fill()
    pen.circle(90)
    pen.end_fill()

    # Draw the bottom curve.
    pen.penup()
    pen.goto(-120, -40)
    pen.pencolor(bgcolor)
    pen.left(140)
    pen.pendown()
    pen.pensize(10)
    
    pen.circle(90, 60)
    
    # Draw the middle curve.
    pen.penup()
    pen.goto(-110, -20)
    pen.pencolor(bgcolor)
    pen.right(60)
    pen.pendown()
    pen.pensize(12)
    
    pen.circle(105, 60)

    # Draw the top curve.
    pen.penup()
    pen.goto(-100, 5)
    pen.pencolor(bgcolor)
    pen.right(60)
    pen.pendown()
    pen.pensize(15)
    
    pen.circle(120, 60)

    # Set text color and write "Spotify".
    pen.penup()
    pen.goto(-40, -60)
    pen.color(circle_color)
    pen.pendown()

    pen.write("Spotify", font=("Arial", 70, "bold"))
    
    # Hide pen.
    pen.hideturtle()


theme = {
            "green": {
                "background": "#ffffff",
                "circle color": "#1db954"
                    },
            "black": {
                "background": "#ffffff",
                "circle color": "#191414"
                    },
            "2-color-green": {
                "background": "#191414",
                "circle color": "#1db954"
                    },
            "2-color-white": {
                "background": "#1db954",
                "circle color": "#ffffff"
                    },
        }

# Read command-line arguments.
parser = argparse.ArgumentParser("Spotify logo animation.")
parser.add_argument("--theme", "-t", default="green", type=str,
                    help="Theme for Spotify logo. [green/black/2-color-green/2-color-white]. DEFAULT='green'")

args = parser.parse_args()
theme_choice = args.theme.lower()

if theme_choice in theme:
    # Initialize the turtle pen and screen objects.
    pen = turtle.Turtle()
    screen = turtle.Screen()

    # Set background color.
    screen.bgcolor(theme[theme_choice]["background"])

    # Draw logo.
    draw_spotify(pen, theme[theme_choice]["background"], theme[theme_choice]["circle color"])

    # Hold screen.
    screen.exitonclick()
else:
    print(f"Invalid theme choice: {theme_choice}")
