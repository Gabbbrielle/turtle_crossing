from turtle import Turtle

import random

Y = random.randint(-280, 280)
X = random.randint(350, 380)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car()
        # self.move()

    def move(self):
        y = random.randint(-280, 280-25)
        x = random.randint(350, 500)
        while -320 < self.xcor() >= -350:
            self.speed("slowest")
            self.forward(STARTING_MOVE_DISTANCE)
        if self.xcor() <= -320:
            self.color(random.choices(COLORS))
            self.ht()
            self.speed('fastest')
            self.penup()
            self.goto(x, y)
            self.st()

    def car(self):
        y = random.randint(-250, 250)
        x = random.randint(350, 400)
        self.ht()
        self.speed('fastest')
        self.penup()
        self.goto(x, y)
        self.shape('square')
        self.shapesize(stretch_wid=.75, stretch_len=1.50)
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.st()
        while True:
            self.move()





