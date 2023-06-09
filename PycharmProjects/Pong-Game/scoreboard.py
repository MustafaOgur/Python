from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", move=False, font=('Courier', 60, 'normal'))
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", move=False, font=('Courier', 60, 'normal'))
