import pandas as pd
import os

# Reading the csv file
data = pd.read_csv(
    r"C:\Users\Jayms\Desktop\Python Programming\ZTM 2024\PROJECTS\Nato_phonetic\nato_phonetic_alphabet.csv"
)

# Create a dictionary comprehension and iterate over it with pandas
phonetic_dict = {series.letter: series.code for (index, series) in data.iterrows()}
# print(phonetic_dict)

# Create a list of the phonetic code that the user input
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
