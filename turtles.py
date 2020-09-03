# Turtle graphics in python

import random
import turtle
from turtle import *

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screen = Screen()
nora = Turtle('turtle')
nora.color('red')
nora.pensize(5)

# nora.setheading(90)
# nora.forward(100)
# nora.left(90)
# nora.forward(100)
# nora.right(90)

def up():
    nora.setheading(90)
    nora.forward(100)

def down():
    nora.setheading(270)
    nora.forward(100)

def left():
    nora.setheading(180)
    nora.forward(100)

def right():
    nora.setheading(0)
    nora.forward(100)

def clickleft(x,y):
    nora.color(random.choice(colors))

def clickright(x,y):
    nora.stamp()

def main():
    turtle.listen()
    turtle.onkey(up, "Up")
    turtle.onkey(down, "Down")
    turtle.onkey(left, "Left")
    turtle.onkey(right, "Right")
    screen.onclick(clickleft, 1)
    screen.onclick(clickright, 3)
    screen.mainloop()

main()