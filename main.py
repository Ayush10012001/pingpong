from turtle import Turtle, Screen
from ball import Ball
from makepaddle import Paddle
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("Ping pong game")

tim=Turtle()
screen.tracer(0)
tim.goto(0,300)
for i in range(40):
    tim.color("white")
    tim.pensize(5)
    tim.setheading(270)
    tim.forward(20)
    tim.penup()
    tim.forward(0)
    tim.pendown()
    tim.hideturtle()

screen.update()
# paddle
screen.tracer(0)
rpaddle=Paddle((470,0))
lpaddle=Paddle((-470,0))
ball = Ball()
scorecard=Scoreboard()
screen.listen()
screen.onkey(rpaddle.goup,"Up")
screen.onkey(rpaddle.godown,"Down")

screen.onkey(lpaddle.goup,"w")
screen.onkey(lpaddle.godown,"s")

gameison=True

while gameison:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bouncey()
    if ball.distance(rpaddle) < 50 and ball.xcor() > 450:  #distance is taken from center of bar so 450 is also specified
        ball.bouncex()
    if ball.distance(lpaddle) < 50 and ball.xcor() < -450:
        ball.bouncex()
    if ball.xcor() > 500:
        scorecard.updateboeardleft()
        ball.ballresetleft()

    if ball.xcor() < -500:
        scorecard.updateboeardright()
        ball.ballresetright()

    if scorecard.lscore==5 or scorecard.rscore==5:
        scorecard.gameover()
        gameison = False






screen.exitonclick()
