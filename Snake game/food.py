from turtle import Turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
class Food(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(random.choice(colors))
        self.shapesize(0.7,0.7)
        self.penup()
        self.speed("fastest")
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
        self.color(random.choice(colors))
        

