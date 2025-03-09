from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed(0)
        self.spawn()

    def spawn(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))



