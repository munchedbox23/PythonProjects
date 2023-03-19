from turtle import Turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_position = [(0,0),(-20,0),(-40,0)]
up = 90
down = 270
right = 0
left = 180
class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self,position):
        snake = Turtle("square")
        snake.color(random.choice(colors))
        snake.penup()
        snake.goto(position)
        self.segment.append(snake)
    
    def extend(self):
        self.add_segment(self.segment[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segment) - 1, 0 , -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.head.forward(20)
    
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
