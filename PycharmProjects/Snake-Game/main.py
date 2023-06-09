from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_over = False
while not game_over:
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()

        scoreboard.score += 1
        scoreboard.update_scoreboard()

        snake.extend()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.game_over()
        game_over = True
        scoreboard.high_score_update()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()
            scoreboard.high_score_update()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
