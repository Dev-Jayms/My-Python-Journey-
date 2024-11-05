"""
I'm working with the readline() and readlines() file attributes.    
"""
# with open("madi.txt", "x", encoding="utf-8") as file:
#     contents = file.write("Madiana\n")
    
with open("madi.txt", "r") as file:
    contents = file.read()
    print(contents)