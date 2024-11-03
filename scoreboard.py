from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.level = 0

    def write_score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def clear_score(self):
        self.clear()

    def inc_score(self):
        self.level += 1

    def game_over(self):
        self.home()
        self.write(f"GAME OVER!", align="center", font=FONT)
