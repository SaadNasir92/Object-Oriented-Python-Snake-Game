from turtle import Turtle

FONT = ('Courier', 18, 'bold')
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.goto(-10, 270)
        self.pencolor('red')
        self.write_score()

    def add_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.clear()
        self.write(f"GAME OVER\nFinal Score: {self.score}", align=ALIGNMENT, font=FONT)

