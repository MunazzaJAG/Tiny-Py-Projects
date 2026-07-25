from turtle import Turtle, Screen
import random, turtle

tim= Turtle()
tim.shape('classic')
turtle.colormode(255)
tim.speed('fast')

def random_color():
    """Returns a random color in RGB format."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw(num_sides):
    """Draws a shape with the specified number of sides."""
    for i in range(num_sides):
        angle= 360/num_sides
        tim.forward(100)
        tim.right(angle)

for i in range(3,11):
    tim.color(random_color())
    draw(i)

screen= Screen()
screen.exitonclick()
