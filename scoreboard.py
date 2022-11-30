from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.goto(-10, 280)
        self.pendown()
        self.pencolor('red')
        self.write_score()

    def add_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score}'), False, 'center', ('Courier', 'bold')
