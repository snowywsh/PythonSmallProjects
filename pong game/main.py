import turtle as tt
import random as rd
import time
from paddle import Paddle
from ball import Ball
from score import Score


screen = tt.Screen()
screen.setup(800, 600)
screen.bgcolor('pale turquoise')
screen.title('My Pong Game')

leftPaddle = Paddle((-350, 0))
rightPaddle = Paddle((350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(rightPaddle.go_up, "-")
screen.onkey(rightPaddle.go_down, "+")
screen.onkey(leftPaddle.go_up, "Up")
screen.onkey(leftPaddle.go_down, "Down")

screen.tracer(0)
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.response)
    ball.move()
    # detect collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    # detect collision with paddle
    if (ball.distance(rightPaddle) < 50 and ball.xcor() >= 330) or (ball.distance(leftPaddle) < 50 and ball.xcor() <= -330):
        ball.bounce_x()
    # detect paddle miss the ball
    if ball.xcor() > 370:
        ball.reset()
        score.l_point()
        if score.leftScore == score.fullPoint:
            score.gameOver()
            game_on = False
    if ball.xcor() < -370:
        ball.reset()
        score.r_point()
        if score.rightScore == score.fullPoint:
            score.gameOver()
            game_on = False



screen.exitonclick()