import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("My turtle crossing game")
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.go_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()
    
    for cars in car.all_cars:
        if(cars.distance(turtle) < 20):
            game_is_on = False
            score.game_over()
    
    if turtle.is_at_finish_line():
        turtle.reset()
        car.level_up()
        score.point()

screen.exitonclick()
