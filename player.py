from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 270

class PlayerStyle(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape('turtle')
        self.st()


class Player(PlayerStyle):
    def __init__(self):
        super().__init__()
        self.move()
        self.again()


    def move(self):
        self.forward(MOVE_DISTANCE)
        self.pos()

    def again(self):
                self.ht()
                self.penup()
                self.goto(STARTING_POSITION)
                self.setheading(90)
                self.st()


