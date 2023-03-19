from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width = 800 , height = 600)
screen.bgcolor("black")
screen.title("New Pong Game")
screen.tracer(0)

paddle = Paddle((0,-150))

ball = Ball()
score = Score()


screen.listen()
screen.onkey(paddle.go_right,"Right")
screen.onkey(paddle.go_left,"Left")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    
    if ball.distance(paddle) < 50 and ball.ycor() < -120 or ball.ycor() > 280:
        ball.bounce_y()
    
    if  ball.ycor() < -180:
        ball.reset_position()
        score.point()
    
    

screen.exitonclick()
