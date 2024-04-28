# Object-Oriented Python Snake Game

## Description
An enhanced rendition of the classic Snake game built with Python and the `turtle` module. This project goes beyond the basics with object-oriented design, featuring a responsive snake that grows, real-time collision detection, and dynamic scoring. Experience a lively game with colorful food objects and a scoreboard to track your high scores.

## Features
- **Object-Oriented Gameplay**: Experience smooth gameplay and object interactions, thanks to a design that leverages Python classes and objects.
- **Dynamic Food Generation**: Food items appear in random locations and colors, providing a vibrant and engaging game environment.
- **Real-Time Collision Detection**: Keep on your toes with collision detections that end the game on wall hits or self-collision.
- **Score Tracking**: Keep track of your current score, with live updates displayed on the screen.

## Technologies Used
- Python
- `turtle` module for graphics and game interface
- Object-oriented programming principles for structuring game components
- `Random` module to randomize food spawns

## External Dependencies
Currently, there are no external dependencies required to run this game, as it utilizes Python's built-in modules exclusively.

## How to Play
1. **Clone the repository to your local machine:**
   ```bash
   git clone https://github.com/SaadNasir92/Object-Oriented-Python-Snake-Game
2. **Navigate to the repository folder**
    ```bash
    cd Object-Oriented-Python-Snake-Game
3. **Run the game**
    ```bash
    python main.py

## Gameplay Instructions
- Use the arrow keys to control the snake.
- Consume food to increase the length of the snake and score points.
- Avoid hitting the walls or the snake's own body.

## Code Example
```python
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
        self.move_made = False

    def grow_snake(self):
        grown_snake = Turtle(visible=False, shape='square')
        grown_snake.penup()
        grown_snake.color('white')
        self.snake_bodies.append(grown_snake)
```
## Lessons Learned
- **Advanced Python Constructs:** Gained deeper insights into Python's turtle module and object-oriented programming.
- **Game Loop and State Management:** Developed an understanding of managing the game loop and the states of game objects.
- **User Input Handling:** Enhanced skills in handling user inputs and responding to key events.

## Future Improvements
- **High Score Persistence:** Implement persistent high score storage using file handling or databases.
- **Enhanced Graphics:** Improve the game's visual appeal with advanced graphics and animations.
- **Sound and Music:** Integrate sound effects and background music to create an immersive gaming experience.
- **Additional Features:** Introduce new levels of difficulty, power-ups, and more interactive game elements.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

