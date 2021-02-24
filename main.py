import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
player = Player()
# screen.tracer(0)
car = CarManager()
screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    car.move()

screen.exitonclick()
