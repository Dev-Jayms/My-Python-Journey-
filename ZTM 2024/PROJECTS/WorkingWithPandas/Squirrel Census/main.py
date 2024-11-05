import pandas
# # Creating a squirrel census csv file.  Creates a CSV file with the count of squirrels by fur color.
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240828.csv")
#
# # Count the number of squirrels by fur color
# gray = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black = len(data[data["Primary Fur Color"] == "Black"])
#
# # Create a dictionary with the count of squirrels by fur color
# squirrels_count = {"color": ["Gray", "Cinnamon", "Black"],
#                     "count": [gray, cinnamon, black]}
#
# # Create a pandas DataFrame from the dictionary
# squirrels_count_df = pandas.DataFrame(squirrels_count)
#
# # Write the DataFrame to a CSV file
# squirrels_count_csv= squirrels_count_df.to_csv("squirrel_count.csv")
#


# print(squirrels_count)
# print(gray)
# print(cinnamon)
# print(black)

# This is the function code of the squirrel census project.

def count_squirrels_by_color(csv_file):
    """
    Reads a squirrel census CSV file and returns a dictionary with the count of squirrels by fur color.

    Args:
        csv_file (str): The path to the squirrel census CSV file.

    Returns:
        dict: A dictionary with the count of squirrels by fur color.
    """
    # Read the squirrel census CSV file into a pandas DataFrame
    data = pandas.read_csv(csv_file)

    # Count the number of squirrels by fur color
    gray = len(data[data["Primary Fur Color"] == "Gray"])
    cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black = len(data[data["Primary Fur Color"] == "Black"])

    # Create a dictionary with the count of squirrels by fur color
    squirrels_count = {"color": ["Gray", "Cinnamon", "Black"],
                       "count": [gray, cinnamon, black]}

    return squirrels_count

def create_squirrel_count_csv(squirrels_count, output_file):
    """
    Creates a CSV file with the count of squirrels by fur color.

    Args:
        squirrels_count (dict): A dictionary with the count of squirrels by fur color.
        output_file (str): The path to the output CSV file.
    """
    # Create a pandas DataFrame from the dictionary
    squirrels_count_df = pandas.DataFrame(squirrels_count)

    # Write the DataFrame to a CSV file
    squirrels_count_df.to_csv(output_file, index=False)

# Usage
csv_file = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240828.csv"
output_file = "squirrel_count.csv"

squirrels_count = count_squirrels_by_color(csv_file)
create_squirrel_count_csv(squirrels_count, output_file)