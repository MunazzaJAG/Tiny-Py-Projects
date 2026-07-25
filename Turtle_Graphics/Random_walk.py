from turtle import Turtle, Screen
import random, turtle

tim= Turtle()
tim.shape('classic')
turtle.colormode(255)
tim.speed('fastest')
tim.pensize(10)

def random_color():
    """Returns a random color in RGB format."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

nos=[0,90,180,270]

for i in range(200):
    tim.color(random_color())
    tim.setheading(random.choice(nos))
    tim.forward(30)

screen= Screen()
screen.exitonclick()
