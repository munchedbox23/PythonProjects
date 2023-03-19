from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()
        
    
    def update_score(self):
        self.clear()
        self.goto(300,250)
        self.write(f"Lose counter: {self.score}" , align= "center" , font= ("Arial",25,"normal"))

    def point(self):
        self.score += 1
        self.update_score()
