from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
