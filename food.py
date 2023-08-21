from turtle import Turtle
import random

class Food(Turtle): # inherit from the Turtle Class
    def __init__(self):
        super().__init__() # inherit from the Turtle Class
        self.shape("circle")
        self. penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("purple")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()


    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
