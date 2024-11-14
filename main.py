from random import random
import turtle as t


tim = t.Turtle()

import random


"""Moving a turtle randomly in right or left direction with changing a color"""

def random_angle():
    angles = [0, 90, 180, 270]
    rand_angle = random.choice(angles)
    return rand_angle

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r/255, g/255, b/255)
    return rand_color

def random_move():
    tim.pensize(10)
    tim.color(random_color())
    tim.forward(40)
    tim.setheading(random_angle())


while True:
    random_move()

