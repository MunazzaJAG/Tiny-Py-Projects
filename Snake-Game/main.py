from turtle import Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# tim.shapesize(0.20,0.60)

snake= Snake()
food= Food()
scoreboard= Scoreboard()

# controlling the snake with keypresses
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score=0

game_on=True
while game_on:
    # update the screen so you don't need to keep watching the segment shift
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect food collisions
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on=False
        scoreboard.game_over()

    #Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.game_over()

screen.exitonclick()
