from turtle import * 
START_POSITION=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self) -> None:
        self.seg=[]
        self.Create_snake()
        self.head=self.seg[0]
    def Create_snake(self):
        for i in START_POSITION:
            nagaraj=Turtle("square")
            nagaraj.color("white")
            nagaraj.penup()
            nagaraj.goto(i)
            self.seg.append(nagaraj)
    def move(self):
        for j in range(len(self.seg)-1,0,-1):
            new_x = self.seg[j-1].xcor()
            new_y = self.seg[j-1].ycor()       
            self.seg[j].goto(new_x, y=new_y)
        self.head.forward((20))
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
                