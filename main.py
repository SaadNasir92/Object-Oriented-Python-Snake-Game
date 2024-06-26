from classes.snake import Snake
from classes.food import Food
from classes.scoreboard import Scoreboard
from turtle import Screen
import time


WALL_COLLISION = 290
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
    snake.move_made = False

    # detecting collision with food.
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.grow_snake()
        scoreboard.add_score()

    # detect collision with wall.
    if snake.head.xcor() > WALL_COLLISION or snake.head.xcor() < -WALL_COLLISION\
            or snake.head.ycor() > WALL_COLLISION or snake.head.ycor() < -WALL_COLLISION:

        game_on = False
        snake.clear()
        food.clear()
        scoreboard.game_over()

    # detect snake collision
    if snake.collision():
        snake.clear()
        food.clear()
        game_on = False
        scoreboard.game_over()

screen.update()
screen.exitonclick()
