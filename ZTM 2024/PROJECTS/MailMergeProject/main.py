# This Python script is reading a list of names from a file called "invited_names.txt" and a letter
# template from a file called "starting_letter.txt". It then replaces a placeholder `[name]` in the
# letter template with each name from the list and creates a personalized letter for each name.

# PLACEHOLDER = "[name]"
#
#
# with open("Input/Names/invited_names.docx", "rb") as names_file:
#     names = names_file.readlines()
#     # print(names)
# with open("Input/Letters/starting_letter.docx","rb") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="wb") as completed_letter:
#             completed_letter.write(new_letter)


"""
This script reads a list of names from a file and a letter template,
then generates personalized letters by replacing a placeholder with each name.
"""

# Define the placeholder to be replaced in the letter template
PLACEHOLDER = "[name]"


def read_names(file_path):

    with open(file_path, "r") as names_file:
        # Read all lines from the file and return them as a list
        return names_file.readlines()


def read_letter_template(file_path):

    with open(file_path, "r") as letter_file:
        # Read the contents of the file and return them as bytes
        return letter_file.read()


def generate_personalized_letters(names, letter_template, placeholder):

    for name in names:
        # Strip any leading or trailing whitespace from the name
        stripped_name = name.strip()
        # Replace the placeholder with the name in the letter template
        new_letter = letter_template.replace(placeholder, stripped_name)
        # Write the personalized letter to a new file
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


# Read the list of names from the file
names = read_names("Input/Names/invited_names.txt")

# Read the letter template from the file
letter_template = read_letter_template("Input/Letters/starting_letter.txt")

# Generate personalized letters
generate_personalized_letters(names, letter_template, PLACEHOLDER)