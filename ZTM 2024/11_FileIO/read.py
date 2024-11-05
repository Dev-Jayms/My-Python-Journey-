""" This code let you read from a file.
    It's also a good habit to write your code in a try() and except() block.
"""

try:
    with open("test2.txt", "r") as file:
        read = file.read()
except FileNotFoundError:
    print("This file doesn'africa exist.")
except FileExistsError:
    print("This file already exist.")
else:
    print(read)
