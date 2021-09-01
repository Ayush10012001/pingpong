from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.goto(-100,190)
        self.write(self.lscore,align="center",font=("courier",50,"normal"))
        self.goto(100, 190)
        self.write(self.rscore, align="center", font=("courier", 50, "normal"))


    def scoreout(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.lscore, align="center", font=("courier", 50, "normal"))
        self.goto(100, 190)
        self.write(self.rscore, align="center", font=("courier", 50, "normal"))

    def updateboeardleft(self):
        self.lscore+=1
        self.scoreout()

    def updateboeardright(self):
        self.rscore += 1
        self.scoreout()

    def gameover(self):
        if self.lscore ==5:
            self.goto(-10,0)
            self.write("GAME OVER \n    LEFT WON", align="center", font=("courier", 50, "normal"))
        elif self.rscore ==5:
            self.goto(0, 0)
            self.write("GAME OVER \n     RIGHT WON", align="center", font=("courier", 50, "normal"))



