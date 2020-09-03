import time
import turtle
import random
from turtle import Turtle, Screen
from random import randint
import operator

tandem_colors = {
    'buoyant_blue': '#A3CCCD',
    'breakthrough_blue': '#0B2D48',
    'sharpie_black': '#1B1B1B',
    'whiteboard_white': '#FFFDFC',
    'ripened_red': '#932C00',
    'graceful_green': '#717244',
    'brash_burgundy': '#8B0444',
    'yearning_yellow': '#FFEC3C',
    'rebellious_red': '#FF694E',
    'growing_green': '#869B8D',
    'talented_tan': '#AF8030',
}

# TODO: why am i writing the same things over and over, stop it
turtle_color_choices = [
    'ripened_red',
    'talented_tan',
    'rebellious_red',
    'growing_green',
    'graceful_green',
    'yearning_yellow',
    'brash_burgundy'
]

starting_heights = {
    1: 100,
    2: 50,
    3: 0,
    4: -50,
    5: -100
}

# TODO: get rid of blinking turtles
# TODO: figure out how to add a property that doesn't belong to turtle already
class RacingTurtle(Turtle):
    def __init__(self, color, starting_height):
        super().__init__(shape='turtle', visible=False)
        self.speed(0)
        self.color(color)
        self.penup()
        self.showturtle()
        self.setpos(-250, starting_height)
        self.pendown()
    def race(self):
        self.forward(randint(1,5))

def setup_screen(screen, color):
    screen.title("Turtle Race")
    screen.bgcolor(color)

def write_title(color):
    title = Turtle()
    title.hideturtle()
    title.color(color)
    title.speed(0)
    title.penup()
    title.setpos(-225, 200)
    title.write("The Great Tandem Turtle Race", font=("Roboto", 30, "bold"))
    title.penup()

def make_sea_floor(color):
    sea_floor = Turtle()
    sea_floor.hideturtle()
    sea_floor.penup()
    sea_floor.setpos(-400, -180)
    sea_floor.color(color)
    sea_floor.begin_fill()
    sea_floor.forward(800)
    sea_floor.right(90)
    sea_floor.forward(300)
    sea_floor.right(90)
    sea_floor.forward(800)
    sea_floor.right(90)
    sea_floor.forward(300)
    sea_floor.end_fill()

def make_finish_line(color):
    stamp_size = 20
    square_size = 15
    finish_line = 200

    finish = Turtle()
    finish.hideturtle()
    finish.speed(0)
    finish.color(color)
    finish.shape('square')
    finish.shapesize(square_size / stamp_size)
    finish.penup()

    for i in range(10):
        finish.setpos(finish_line, (150 - (i * square_size * 2)))
        finish.stamp()

    for j in range(10):
        finish.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
        finish.stamp()

def run_the_race(turtles):
    for i in range(145):
        turtles[0].race()
        turtles[1].race()
        turtles[2].race()
        turtles[3].race()
        turtles[4].race()

def get_winner(turtles):
    final_positions = {
        1: turtles[0].xcor(),
        2: turtles[1].xcor(),
        3: turtles[2].xcor(),
        4: turtles[3].xcor(),
        5: turtles[4].xcor()
    }
    # TODO: Need to handle a tie!
    return max(final_positions.items(), key=operator.itemgetter(1))[0]

def reveal_winner(winner, color):
    result = Turtle()
    result.hideturtle()
    result.penup()
    result.setpos(-180, -275)
    result.color(color)
    result.write(f"Congratulations, {winner}!!", font=("Roboto", 30, "bold"))
    result.penup()

# TODO: get a countdown??

def get_turtle_info(color_choices):
    print('For each of the five turtles, please enter a name and color.')
    print()
    messages = ["Get ready", "On your marks", "Look sharp", "Warm up"]
    turtles = dict.fromkeys(range(1,6))
    for i in range(1,6):
        print(f"Turtle {i}:")
        name = input("Name: ")
        print()
        print(f"Color choices: {color_choices}")
        color = input("Color: ")
        color_choices.remove(color)
        turtles[i] = (name, color)
        print()
        print(f'>>>>>>>> {random.choice(messages)}, {name}! <<<<<<<<')
        print()
        print("-------------------")
        print()
    return turtles

def main():
    print()
    print('The Great Tandem Turtle Race')
    print("----------------------------")
    print()
    print('Five competitors...may the best Turtle win.')
    print()
    screen = Screen()

    setup_screen(screen, tandem_colors['breakthrough_blue'])
    write_title(tandem_colors['buoyant_blue'])

    make_sea_floor(tandem_colors['buoyant_blue'])
    make_finish_line(tandem_colors['whiteboard_white'])

    all_the_turtles = get_turtle_info(turtle_color_choices)
    print()
    print('On your marks...')

    one = RacingTurtle(tandem_colors[all_the_turtles[1][1]], starting_heights[1])
    two = RacingTurtle(tandem_colors[all_the_turtles[2][1]], starting_heights[2])
    three = RacingTurtle(tandem_colors[all_the_turtles[3][1]], starting_heights[3])
    four = RacingTurtle(tandem_colors[all_the_turtles[4][1]], starting_heights[4])
    five = RacingTurtle(tandem_colors[all_the_turtles[5][1]], starting_heights[5])
    
    racing_turtles = [one, two, three, four, five]
    print()
    print('.....Get set....')
    time.sleep(3) # pause the game for one second before starting the race

    print()
    print("......GO!")
    run_the_race(racing_turtles)

    winner = get_winner(racing_turtles)
    winner_name = all_the_turtles[winner][0]
    winner_color = tandem_colors[all_the_turtles[winner][1]]
    reveal_winner(winner_name, winner_color)

    screen.exitonclick()
    screen.mainloop()

main()
