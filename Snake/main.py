from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
# Objects
food = Food()
screen = Screen()
scoreboard = Scoreboard()
snake = Snake()

#Object set-up
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



#Controls
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.spawn()
        snake.extend()
        scoreboard.increase_score()
    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.ycor() >295 or snake.head.xcor() < -295 or snake.head.ycor() < - 295:
        scoreboard.game_over()
        game_is_on = False
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False





















screen.exitonclick()