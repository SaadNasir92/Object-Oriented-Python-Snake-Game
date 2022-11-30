from turtle import Turtle


class Snake:

    def __init__(self):
        start_x = 20
        self.snake_bodies = []
        for _ in range(3):
            squares = Turtle(shape='square')
            squares.penup()
            squares.color('white')
            squares.goto(start_x, 0)
            start_x -= 20
            self.snake_bodies.append(squares)
        self.head = self.snake_bodies[0]

    def move(self):
        for body in range(len(self.snake_bodies) - 1, 0, -1):
            self.snake_bodies[body].goto(self.snake_bodies[body - 1].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
