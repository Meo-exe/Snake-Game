from turtle import Turtle, Screen

STARTING_POSITION = [(0,0), (0,-20), (0,-40)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    MOVE_INC = 20


    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]



    def create(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].goto(self.segments[seg - 1].xcor(), self.segments[seg - 1].ycor())
        self.head.forward(self.MOVE_INC)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
           self.head.seth(UP)
    def down(self):
        if self.head.heading() != UP:
           self.head.seth(DOWN)




