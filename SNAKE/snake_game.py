from turtle import Screen
import time
from food import Food
from snake import Snake
from score import scoreboard
sc=Screen()
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.title("The Snake Game")
sc.tracer(0)
s=Snake()
f=Food()
scores=scoreboard()
sc.listen()
sc.onkey(s.up, "Up")
sc.onkey(s.down, "Down")
sc.onkey(s.right, "Right")
sc.onkey(s.left, "Left")

game=1
i=0
while game:
    sc.update()
    time.sleep(0.1)
    s.move()
    if s.head.distance(f)<15:
        f.refresh()
        i+=1
        scores.increase()
    if s.head.xcor()<-280 or s.head.xcor()>280 or s.head.ycor()<-280 or s.head.ycor()>280:
        game=0
        scores.game()

sc.exitonclick()