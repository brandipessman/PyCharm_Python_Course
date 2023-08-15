# from turtle import Turtle, Screen
import random
# from turtle import * to import all
import turtle as t #lets you rename the module
# import turtle forces you to write turtle.Turtle
# import heroes
# print(heroes.gen())
import colorgram
import colorgram.colorgram

tim = t.Turtle()
t.colormode(255)
#tim.shape("turtle")
tim.color("black")
### Draw a square ###
# for number in range(1,5):
#     tim.forward(100)
#     tim.right(90)

### Dashed line, no line, filled line ###
# for number in range(1, 11):
#     tim.pencolor("black")
#     tim.forward(2)
#     tim.penup()
#     tim.forward(2)
#     tim.pendown()
#
# tim.penup()
# tim.forward(40)
# tim.pendown()
# tim.forward(40)

### Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon ###
# for number in range(3, 11):
#     times = number
#     while times != 0:
#         tim.color(random.choice(colors))
#         tim.forward(30)
#         tim.right(360 / number)
#         times -= 1

### Draw a random walk ###
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# for number in range(100):
#     tim.color(random_color())
#     tim.width(6)
#     tim.speed(5)
#     tim.forward(20)
#     tim.right(90 * random.randint(0, 4))

### Draw a spirograph ###
# tim.speed(100)
# for number in range(60):
#     tim.circle(100)
#     tim.right(6)
#     tim.color(random_color())


colors = colorgram.extract('fall_trees.jpeg', 10)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

screen = t.Screen()
tim.hideturtle()
tim.speed(200)
tim.penup()
tim.setheading(225)
tim.forward(320)
tim.setheading(0)
def draw_line():
    for number in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.penup()
        tim.forward(50)

def new_row():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

draw_line()
for number in range(9):
    new_row()
    draw_line()

screen.exitonclick()
