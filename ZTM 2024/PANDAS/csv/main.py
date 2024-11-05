"""
REMOVING EMPTY CELLS
Empty cells can potentially give you a wrong result when you analyze data.

Remove Rows
One way to deal with empty cells is to remove rows that contain empty cells.

This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
"""
import pandas as pd
df = pd.read_csv('data.csv')
# new_df = df.dropna()
# df.loc[7, 'Duration'] = 45 #This remove the typo of 450 in row 7 to 45

# print(df.duplicated()) #Returns True for every row that is a duplicate, otherwise False:
df.drop_duplicates(inplace = True) #To remove duplicates
print(df.to_string())