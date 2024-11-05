"""
Africa Countries Game

This script simulates a game where the user has to guess the names of African countries.
The game uses a turtle graphics window to display a map of Africa and mark the guessed countries.
"""

import turtle
import pandas
import time


def load_country_data(file_name: str) -> pandas.DataFrame:
    """
    Load country data from a CSV file.

    Args:
        file_name (str): The name of the CSV file containing the country data.

    Returns:
        pandas.DataFrame: A DataFrame containing the country data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    try:
        data = pandas.read_csv(file_name)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        exit()

    # Check if the 'countries' column exists in the DataFrame
    if 'countries' not in data.columns:
        print("Error: 'countries' column not found in CSV file.")
        exit()

    return data


def get_missing_countries(all_countries: list, guessed_countries: list) -> list:
    """
    Get a list of countries that have not been guessed yet.

    Args:
        all_countries (list): A list of all countries.
        guessed_countries (list): A list of countries that have already been guessed.

    Returns:
        list: A list of countries that have not been guessed yet.
    """
    missing_countries = []
    for district in all_countries:
        if district not in guessed_countries:
            missing_countries.append(district)
    return missing_countries


def save_missing_countries(missing_countries: list, file_name: str) -> None:
    """
    Save a list of missing countries to a CSV file.

    Args:
        missing_countries (list): A list of countries that have not been guessed yet.
        file_name (str): The name of the CSV file to save the missing countries to.

    Raises:
        Exception: If an error occurs while saving the file.
    """
    new_data = pandas.DataFrame(missing_countries)
    try:
        new_data.to_csv(file_name)
    except Exception as e:
        print(f"Error: Unable to write to file '{file_name}': {e}")


def main() -> None:
    # Set up the turtle graphics window
    screen = turtle.Screen()
    screen.title("Africa Countries Game")
    image = "MAPAfrica.gif"
    screen.addshape(image)
    turtle.shape(image)

    # Load country data from CSV file
    data = load_country_data("54_countries.csv")

    # Get a list of all countries
    all_countries = data.countries.to_list()
    guessed_countries = []

    # Start the game timer
    start_time = time.time()

    while len(guessed_countries) < 50:
        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)

        # Ask the user for a country name
        answer_countries = screen.textinput(title=f"{len(guessed_countries)}/54 Countries Correct",
                                            prompt=f"What's another country's name? Time spent: {int(minutes):02d}:{seconds:05.2f}").title()

        # Check if the user wants to exit the game
        if answer_countries == "Exit":
            # Get a list of missing countries
            missing_countries = get_missing_countries(all_countries, guessed_countries)
            # Save the missing countries to a CSV file
            save_missing_countries(missing_countries, "countries_to_learn.csv")
            break

        # Check if the country name is valid
        if answer_countries in all_countries:
            # Check if the country has already been guessed
            if answer_countries not in guessed_countries:
                # Add the country to the list of guessed countries
                guessed_countries.append(answer_countries)

                # Create a new turtle to mark the country on the map
                africa = turtle.Turtle()
                africa.hideturtle()
                africa.penup()

                # Get the coordinates of the country
                country_data = data[data.countries == answer_countries]
                if not country_data.empty:
                    # Move the turtle to the country's coordinates and write the country name
                    africa.goto(int(country_data.x), int(country_data.y))
                    africa.write(answer_countries)
                else:
                    print(f"Error: Unable to find country '{answer_countries}' in data.")
            else:
                print(f"Error: You've already guessed the country '{answer_countries}'. Try again.")


if __name__ == "__main__":
    main()


