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


names = []
num = 1
for create_car in range(5):
    name = "car_" + str(num)
    names.append(name)
    num = num + 1
print(names)
cars = []
for name in names:
    name = CarManager()
    cars.append(name)
# print(cars)
# cars[0].move()
# cars[1].move()
# cars[2].move()
# cars[3].move()
# cars[4].move()





screen.listen()
screen.onkey(player.move, "Up")
# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()


screen.exitonclick()
