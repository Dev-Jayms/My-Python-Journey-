\
import json
"""
This codes generate a JSON LOADS and JSON DUMPS
"""

usernames = input("Whats's your name?: ")
with open("usernames.json", "a") as file:
    json.dump(usernames,file)
        
        
with open("usernames.json") as file:
    contents = json.load(file)
    print(contents)