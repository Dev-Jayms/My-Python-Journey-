import pandas as pd

# Load the JSON file into a DataFrame:
df = pd.read_json("data.json")
print(df.to_string())
# print(df.head(10)) #Get a quick overview by printing the first 10 rows of the DataFrame:
#print(df.tail(10)) #a tail() method for viewing the last rows of the DataFrame.:
# print(df.describe())
print(df.info())

# import os

# print(os.getcwd())
