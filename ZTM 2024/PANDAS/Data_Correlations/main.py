"""This searches for a relationship between the columns"""
import pandas as pd
df=pd.read_csv('data.csv')
print(df.corr()) #Show the relationship between the columns: