from turtle import Screen
import time
from snake import Snake
from food import  Food
from score import ScoreBoard

my_screen = Screen()
my_screen.setup(600,600)
my_screen.bgcolor("black")
my_screen.tracer(0)

my_snake = Snake()
food = Food()
score = ScoreBoard()

my_screen.listen()
my_screen.onkey(my_snake.moveup, "Up")
my_screen.onkey(my_snake.movedowm, "Down")
my_screen.onkey(my_snake.moveleft, "Left")
my_screen.onkey(my_snake.moveright, "Right")


is_on = True
while is_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()
    if my_snake.head.distance(food) < 15:
        food.refresh_newdot()
        score.scorecount()
        my_snake.extend()

    if my_snake.head.xcor() >= 300 or my_snake.head.xcor() <= -300 or my_snake.head.ycor() >= 300 or my_snake.head.ycor() <= -300:
        is_on = False
        score.gameover()


    for seg in my_snake.segments[1:]:
        if my_snake.head.distance(seg) < 10:
            is_on = False
            score.gameover()
















my_screen.exitonclick()

