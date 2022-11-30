from data import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

# Making food and snake objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detecting collision with food.
    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.add_score()


screen.exitonclick()
