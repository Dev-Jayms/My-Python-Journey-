import os
"""
READ FILE AND EXCEPTION
"""

class ReadMe:
    def __init__(self):
        pass
    try:
        def readme():
            """This function code read the words in the file."""
            with open("WorkingWithFiles/file.csv", "r") as file:
                content= file.read()
            print(content)
        readme()
    except:
        print("The file doesn'africa exist.")

#This code delete a file
# os.remove("file.csv")

if os.path.exists("James.txt"):
    os.remove("James.txt")
else:
    print("The file does not exist.")