from turtle import Turtle


class Snake:

    def __init__(self):
        start_x = 20
        self.snake_bodies = []
        for _ in range(20):
            squares = Turtle(shape='square')
            squares.penup()
            squares.color('white')
            squares.goto(start_x, 0)
            start_x -= 20
            self.snake_bodies.append(squares)
        self.head = self.snake_bodies[0]
        self.move_made = False

    def grow_snake(self):
        grown_snake = Turtle(visible=False, shape='square')
        grown_snake.penup()
        grown_snake.color('white')
        self.snake_bodies.append(grown_snake)

    def move(self):
        for body in range(len(self.snake_bodies) - 1, 0, -1):
            self.snake_bodies[body].showturtle()
            self.snake_bodies[body].goto(self.snake_bodies[body - 1].pos())
        self.head.forward(20)

    def collision(self):
        for body in self.snake_bodies[1:]:
            if self.head.distance(body) < 1:
                return True

    def up(self):
        if (self.head.heading() != 270 and self.head.heading() != 90) and not self.move_made:
            self.head.setheading(90)
            self.move_made = True

    def down(self):
        if (self.head.heading() != 270 and self.head.heading() != 90) and not self.move_made:
            self.head.setheading(270)
            self.move_made = True

    def left(self):
        if (self.head.heading() != 0 and self.head.heading() != 180) and not self.move_made:
            self.head.setheading(180)
            self.move_made = True

    def right(self):
        if (self.head.heading() != 0 and self.head.heading() != 180) and not self.move_made:
            self.head.setheading(0)
            self.move_made = True

    def clear(self):
        for obj in self.snake_bodies:
            obj.hideturtle()
