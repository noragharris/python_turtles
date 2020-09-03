import turtle
import random
from turtle import Turtle, Screen

screen = Screen()
t = Turtle('arrow', visible=False)
t.speed(-1)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
t.color(random.choice(colors))

TURTLE_SIZE = 20

def script(x, y):
    t.pendown()
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(script)

def lift(x, y):
    t.penup()
    screen.onclick(t.goto)

def start():
    t.penup()
    t.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
    t.pendown()
    t.showturtle()

def main():
    turtle.listen()
    start()
    t.ondrag(script)
    t.onrelease(lift)
    screen.mainloop()

main()
