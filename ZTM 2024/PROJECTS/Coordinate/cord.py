import turtle
import pandas

screen = turtle.Screen()
screen.title("Salone District Game")
image = "MAPAfrica.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

screen = turtle.Screen()
screen.onscreenclick(get_mouse_click_coor)
screen.mainloop()