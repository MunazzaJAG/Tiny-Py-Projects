from turtle import Turtle, Screen
import random, turtle

tim= Turtle()
tim.shape('classic')
turtle.colormode(255)
tim.speed('fastest')
tim.pensize(2)

def random_color():
    """Returns a random color in RGB format."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(10)

screen= Screen()
screen.exitonclick()