from turtle import Turtle, Screen
import random
race=0
screen=Screen()
screen.setup(width=1000,height=400)
user=screen.textinput(title="Make your bet",prompt="Which tutle will win the race? Enter a color: ")
colors=["red","orange","yellow","green","blue","purple"]
ypos=[-70,-40,-10,20,50,80]
ypo=[-200,-150,-100,-50,0,50,100,150,200,170]
all_turtle=[]
for i in range(0,6):
    k=Turtle(shape="turtle")
    k.penup()
    k.color(colors[i])
    k.goto(x=-450,y=ypos[i])
    all_turtle.append(k)
for i in range(0,9):
    d=Turtle(shape="arrow")
    d.penup()
    d.goto(x=470,y=ypo[i])
if user:
    race=1
while race:
    for i in all_turtle:
        if i.xcor()>450:
            win=i.pencolor()
            if(win==user):
                print("You have won!")
            else:
                print("you have lost.")
            print(f"The {win} turtle is winner")
            race=0
            break
        dis=random.randint(0,10)
        i.forward((dis))
    
screen.exitonclick()