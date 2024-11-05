import turtle
import pandas

# Load country data
data = pandas.read_csv("countries.csv")

# Create a turtle screen
screen = turtle.Screen()
screen.title("Country Guessing Game")

# Create a turtle to write text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()

# Initialize score
score = 0

# Function to check the answer
def check_answer(country, capital):
    global score
    for index, row in data.iterrows():
        if row["Country"].lower() == country.lower() and row["Capital"].lower() == capital.lower():
            score += 1
            return True
    return False

# Function to play the game
def play_game():
    global score
    text_turtle.clear()
    country = screen.textinput("Country", "Enter the name of a country: ")
    capital = screen.textinput("Capital", "Enter the capital of the country: ")
    if check_answer(country, capital):
        text_turtle.write("Correct! Your score is " + str(score), align="center", font=("Arial", 24, "normal"))
    else:
        text_turtle.write("Incorrect. The correct answer is " + data.loc[data["Country"] == country, "Capital"].values[0] + ". Your score is " + str(score), align="center", font=("Arial", 24, "normal"))
    screen.ontimer(play_game, 2000)

# Start the game
text_turtle.write("Welcome to the country guessing game! Enter the name of a country and its capital.", align="center", font=("Arial", 24, "normal"))
screen.ontimer(play_game, 2000)

turtle.mainloop()