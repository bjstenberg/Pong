from ball import Ball
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ponggers")
screen.tracer(0)

GAME_OVER = 10

l_paddle = Paddle((-360, 0))
r_paddle = Paddle((360, 0))
ball = Ball()
scoreboard = Scoreboard()
ball.color("green")

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 63 and ball.xcor() > 340:
        ball.setx(340)
        ball.bounce_x()

    if ball.distance(l_paddle) < 63 and ball.xcor() < -340:
        ball.setx(-340)
        ball.bounce_x()

    # Detect right paddle collision
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == GAME_OVER:
        winner = "left player"
        scoreboard.end(winner)
        game_on = False
    elif scoreboard.r_score == GAME_OVER:
        winner = "right player"
        scoreboard.end(winner)
        game_on = False

screen.exitonclick()