from turtle import Turtle



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scorevoard = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.scorecount()

    def scorecount(self):
        self.clear()
        self.write(arg=f"Score = {self.scorevoard}   High score = {self.highscore}", move=False, align="center", font=("Arial",15,"normal"))
        self.scorevoard += 1

    def reset_game(self):
        if self.scorevoard > self.highscore:
            self.highscore = self.scorevoard
