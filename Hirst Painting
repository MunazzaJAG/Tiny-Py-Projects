import colorgram
import turtle as t
import random

rgb=[]
colors = colorgram.extract('image.jpg', 6)
for color in colors:
    r= color.rgb.r
    g= color.rgb.g
    b= color.rgb.b
    new= (r,g,b)
    rgb.append(new)

tim= t.Turtle()
t.colormode(255)
tim.speed("fastest")

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for i in range(10):
    for j in range(10):
        tim.pendown()
        tim.dot(20,random.choice(rgb))
        tim.penup()
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
print(rgb)
