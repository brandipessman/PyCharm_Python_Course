from turtle import Turtle, Screen
import random

# tim = Turtle()
screen = Screen()

### Etch-a-Sketch###
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def move_counter():
#     tim.left(15)
#
# def move_clock():
#     tim.right(15)
#
# def move_clear():
#     tim.reset()
#
# screen.listen()
# screen.onkey(key = "w", fun = move_forward)
# screen.onkey(key = "s", fun = move_backward)
# screen.onkey(key = "a", fun = move_counter)
# screen.onkey(key = "d", fun = move_clock)
# screen.onkey(key = "c", fun = move_clear)
# screen.exitonclick()

### Turtle Race ###
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet.", prompt = "Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_start = -100
all_turtles = []

for color in colors:
    new_color = color
    new_color = Turtle(shape = "turtle")
    new_color.color(color)
    new_color.penup()
    new_color.goto(x = -225, y = y_start)
    y_start += 40
    all_turtles.append(new_color)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()