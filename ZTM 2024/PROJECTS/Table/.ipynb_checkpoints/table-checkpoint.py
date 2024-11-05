from prettytable import PrettyTable

# # Create a new table
# table = PrettyTable()

# # Add column headers
# table.field_names = ["Name", "Age", "City"]

# # Add rows to the table
# table.add_row(["Alice", 25, "New York"])
# table.add_row(["Bob", 30, "London"])
# table.add_row(["Charlie", 35, "Paris"])
# table.add_row(["James", 35, "Paris"])
# table.add_row(["Rashida", 15, "Bath"])

# # Print the table
# print(table)

# '''
# This code defines a function create_table that takes a list of rows as input, creates a table with the specified column headers, and adds the rows to the table. Finally, it prints the table.

# You can call the function with your own data to create a table.'''


def create_table(data):
    # Create a new table
    table = PrettyTable()

    # Add column headers
    table.field_names = ["Name", "Age", "City"]

    # Add rows to the table
    for row in data:
        table.add_row(row)

    # Align the column headers
    table.align = "l"
    # table.border = True

    # Print the table
    print(table)


# Adding data to the table:
data = [
    ["James", 32, "Freetown"],
    ["Binta", 31, "London"],
    ["Rashida", 5, "Paris"],
    ["Mohamed", 3, "Bath"],
    ["Madiana", 1, "New York"]
]

create_table(data)
# print(data[2])
