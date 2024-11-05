
import turtle as t
import random


"""This code make the turtle create a random walk with different colours"""


def ran_walk():
    tim = t.Turtle()
    colour = t.colormode(255)
    # This function create the Random color for the randomwalk.
    def random_colour():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)
        return random_color


# colours = ["CornFlowerBlue", "DarkOrchid","IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

    direction = [0,90,180,270]
    tim.pensize(12)
    tim.speed("fastest")

    for _ in range(200):
        tim.color(random_colour())
        tim.forward(30)
        tim.setheading(random.choice(direction))

ran_walk()