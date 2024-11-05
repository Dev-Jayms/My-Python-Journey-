"""import the turtle module and random module"""
import turtle as t
import random

"""This draw a spirography with the turtle"""
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)



def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
screen=t.Screen()
screen.exitonclick()
