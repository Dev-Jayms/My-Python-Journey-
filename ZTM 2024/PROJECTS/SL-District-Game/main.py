import turtle
import pandas

screen = turtle.Screen()
screen.title("Sierra Leone District Game")
image = "blank_salone_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("16_districts.csv")
all_districts = data.districts.to_list()
guessed_districts = []

while len(guessed_districts) < 50:
    answer_districts = screen.textinput(title=f"{len(guessed_districts)}/16 Districts Correct",
                                        prompt="What's another district's name?").title()
    if answer_districts == "Exit":
        missing_districts = []
        for district in all_districts:
            if district not in guessed_districts:
                missing_districts.append(district)
        new_data = pandas.DataFrame(missing_districts)
        new_data.to_csv("districts_to_learn.csv")
        break
    if answer_districts in all_districts:
        guessed_districts.append(answer_districts)
        salone = turtle.Turtle()
        salone.hideturtle()
        salone.penup()
        district_data = data[data.districts == answer_districts]
        salone.goto(int(district_data.x), int(district_data.y))
        salone.write(answer_districts)
