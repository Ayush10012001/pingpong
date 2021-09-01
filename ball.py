from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.goto(0,0)
        self.xvalue = 10
        self.yvalue = 10
        self.movespeed=0.1

    def move(self):
        newx=self.xcor() + self.xvalue
        newy = self.ycor() + self.yvalue
        self.penup()
        self.goto(newx,newy)

    def bouncey(self):
        self.yvalue *= -1
        self.movespeed*=0.9

    def bouncex(self):
        self.xvalue *= -1
        self.movespeed *= 0.9

    def ballresetleft(self):
        self.goto(0, 0)
        self.xvalue *= -1
        self.movespeed = 0.09

    def ballresetright(self):
        self.goto(0, 0)
        self.xvalue *= -1
        self.movespeed = 0.1

