COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
random_size = random.randint(1,10)
random_x = random.randint(-280,280)
random_y = random.randint(-280,280)

class CarManager:
    

    def __init__(self):
        self.all_cars = list()
        self.car_speed = STARTING_MOVE_DISTANCE
        

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=3)
            new_car.goto(300,random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
