from turtle import Turtle
STARTING_POS=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
UP= 90
DOWN= 270
LEFT= 180
RIGHT= 0

class Snake:
    def __init__(self):
        self.segments=[]
        self.createSnake()
        self.head= self.segments[0]

    def createSnake(self):
        for i in STARTING_POS:
            self.add_segment(i)

    def add_segment(self,position):
        tim = Turtle(shape="circle")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            # cors= segments[seg_no-1]
            x_cor = self.segments[seg_no - 1].xcor()
            y_cor = self.segments[seg_no - 1].ycor()
            new_seg = self.segments[seg_no].goto(x_cor, y_cor)

        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != LEFT:
            self.head.setheading(LEFT)
