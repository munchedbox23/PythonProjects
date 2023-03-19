FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-220,260)
        self.write(f"Level: {self.score}" , align= "left",font = FONT)

    def point(self):
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align ="center", font = FONT)
        
