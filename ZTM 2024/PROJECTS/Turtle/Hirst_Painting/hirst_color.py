import colorgram
import turtle as t
import random

from pygame.examples.scrap_clipboard import screen
from sqlalchemy.testing.pickleable import Screen

#
# rgb_color = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
#
# print(rgb_color)


t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(185, 156, 32), (120, 38, 73), (208, 82, 92), (21, 49, 116), (171, 90, 27), (45, 114, 156), (160, 61, 89), (246, 247, 250), (61, 42, 36), (246, 249, 248), (51, 35, 41), (34, 80, 70), (177, 28, 27), (93, 127, 165), (25, 34, 86), (204, 120, 132), (27, 59, 50), (135, 156, 180), (207, 74, 69), (233, 204, 119), (71, 103, 78), (154, 170, 161), (231, 168, 176), (228, 172, 165), (177, 186, 216), (66, 116, 4), (12, 79, 110)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
