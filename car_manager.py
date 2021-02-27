from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


Y = 260
Y_RANGE = random.randint(-Y, Y)
X_RANGE = random.randint(350, 380)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManagement:
    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def car(self):
        random_chance = random.randint(1, 6)
        y = random.randint(-250, 250)
        if random_chance == 1:
            unit = Turtle("square")
            unit.shapesize(stretch_wid=.75, stretch_len=1.50)
            unit.penup()
            unit.color(random.choice(COLORS))
            unit.goto(320, y)
            unit.setheading(180)
            self.cars.append(unit)

    def move(self):
        for car in self.cars:
            car.speed('slowest')
            car.forward(self.move_speed)

    def faster(self):
        self.move_speed += MOVE_INCREMENT
