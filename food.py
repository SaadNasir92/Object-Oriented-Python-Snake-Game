import turtle
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        turtle.colormode(255)
        self.rand_color()
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 265)
        random_y = random.randint(-270, 265)
        self.rand_color()
        self.goto(random_x, random_y)

    def rand_color(self):
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        color = (r, g, b)
        self.color(color)
