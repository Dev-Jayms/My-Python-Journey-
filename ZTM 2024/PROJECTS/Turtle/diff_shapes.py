from turtle import Turtle
import random
# Make the turtle draw different shapes with different colors
tim = Turtle()

colours = ["CornFlowerBlue", "DarkOrchid","IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shapes(sides):
    angle = 360/sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)
for shape_side in range(3,11):
    tim.color(random.choice(colours))
    draw_shapes(shape_side)

