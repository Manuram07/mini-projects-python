from turtle import Turtle
class scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.increase()
        self.hideturtle()
    def game(self):
        self.goto(0,0)
        self.write("Game Over",align=("center"),font=("Arial",22,"normal"))
        
    def increase(self):
        self.clear()
        self.write(f"Score :{self.score}",align=("center"),font=("Arial",22,"normal"))
        self.score+=1
        