from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_right.go_up, "Up")
screen.onkeypress(paddle_right.go_down, "Down")
screen.onkeypress(paddle_left.go_up, "w")
screen.onkeypress(paddle_left.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect the collision with the right_paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        # print("Hit the r_paddle")

    #Detect if the right paddle missed the ball
    if ball.xcor() > 380:
        # print("Miss the paddle")
        ball.reset_position()
        scoreboard.l_point()

    # Detect if the left paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()