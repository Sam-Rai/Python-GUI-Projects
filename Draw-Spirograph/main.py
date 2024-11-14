import random
import turtle as t


tim = t.Turtle()

"""Creating a random rgb color"""
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rand_color = (r/255, g/255, b/255)
    return rand_color

tim.speed("fastest")

"""Drawing a spirograph"""
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(150)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
