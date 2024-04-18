from turtle import Turtle , Screen
import time
from snake import Snake
from food import Food
from score_board import score

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = score()

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
count = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
#   detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.stop_game()

    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
           game_is_on = False
           score_board.stop_game()


screen.exitonclick()