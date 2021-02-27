import time
from turtle import Screen
from player import Player
from car_manager import CarManagement
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
player = Player()
score = Scoreboard()
screen.tracer(0)
crusher = CarManagement()

screen.listen()
screen.onkeypress(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    crusher.car()
    crusher.move()
    if player.ycor() >= 270:
        player.again()
        score.refresh()
        crusher.faster()
    for car in crusher.cars:
        if car.distance(player) <= 20:
            game_is_on = False
            score.game_over()



screen.exitonclick()
