""" This code let you write to a file.
    It's also a good habit to write your code in a try() and except() block.
"""

try:
    with open("test2.txt", mode="a", encoding="utf-8") as file:
        text = file.write("My name is James Konomanyi.\nI'm a software developer.")
except FileExistsError:
    print("This file already exist.")
except FileNotFoundError:
    print("This file doesn'africa exist.")