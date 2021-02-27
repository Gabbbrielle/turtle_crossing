FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.play_time = 10
        self.score = 0
        self.ht()
        self.color('black')
        self.speed('fastest')
        self.penup()
        self.goto(-150, 260)
        self.write(f'score: {self.score} ', False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align='center', font=FONT)

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f'score: {self.score} ', False, ALIGNMENT, FONT)


