"""Iteration over a pandas DataFrame"""

import pandas as pd

# Students dictionary
students_data = {"student": ["James", "Binta", "Tina"], "score": [90, 89, 98]}

# Converting the dictionary to pandas Data Frame
students_data_frame = pd.DataFrame(students_data)
# print(students_data_frame)

# Loop through a data frame
for index, series in students_data_frame.iterrows():
    if (series.student) == "James":
        print(series.score)

# This output the student with the highest mark
#   if (series.score) >= 95:
#     print(series.student, "is the only student with", series.score, "marks.")

# print(series.student) #This print out the student name
# print(series.score) #This print out the student score
