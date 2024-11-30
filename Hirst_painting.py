import turtle as t
import random as ra
# n=int(input())
sc=t.Screen()
k=t.turtles
t.colormode(255)
def col():
    r=ra.randint(0, 255)
    g=ra.randint(0, 255)
    b=ra.randint(0, 255)
    return r,b,g
def turn():
    k=t.left(90)
    k=t.forward(20)
    k=t.left(90)
    k=t.forward(210)
    k=t.right(180)
t.pensize(10)
for i in range(10): 
    for j in range(20):
        k=t.color(col())
        if j%2==0:
            k=t.pendown()
            k=t.forward(1)
            
        else:
            k=t.penup()
            t.forward(20)
    t.penup()
    turn()
    
sc.exitonclick()
