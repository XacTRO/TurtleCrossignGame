import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

cars = []

score = Scoreboard()

car_manager = CarManager()
screen.listen()
screen.onkey(fun=player.move_forward, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    score.write_score()
    car_manager.move_cars()

    if player.start_again():
        score.clear_score()
        score.inc_score()
        car_manager.change_speed()

    if car_manager.game_over(player):
        game_is_on = False
        score.game_over()

    player.start_again()

screen.exitonclick()
