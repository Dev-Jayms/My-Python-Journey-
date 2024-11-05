import os
"""
This code add more words in the file. to the existing words.
"""
# from encodings import utf_8

# with open ("WorkingWithFiles/file.csv", "a") as file:
#     CONTENT = "\nMadiana   1 "
#     file.write(CONTENT)


def writeme():   
    """#This code overwrite all the names in the file.txt file"""
    with open("WorkingWithFiles/file.txt", "w") as file:
        content = "This code overwrite all the names in the txt file.2"
        file.write(content)
writeme()   

# def createme():
#     with open("file3.txt", "x") as file:
#         contents = file.write("This create a new file2.txt in our current folder.")
# createme()

def readme():
    """This function code read the words in the file."""
    with open("WorkingWithFiles/file.csv", "r") as file:
        content= file.read()
    print(content)
readme()

#This code delete a file
# os.remove("file.csv")

if os.path.exists("James.txt"):
    os.remove("James.txt")
else:
    print("The file does not exist.")
