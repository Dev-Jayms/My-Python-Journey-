'''Import csv, and then read the csv file from the file path'''
import pandas as pd

# Read the csv file
print('\nRead the csv file')
data = pd.read_csv('weather_data.csv')
print(data)

# This gives the average temperature of the week
print('\nThis gives us the average temperature')
print(data["temp"].mean())
#
# This convert the data to a dictionary
print('\nThis convert the data to a dictionary')
data_dict = data.to_dict()
print(data_dict)

# This convert the data to a list
print('\nThis convert the data to a list')
data_list = data['temp'].to_list()
print(data_list)

# Get data in Row
print('\nGet data in Row')
print(data[data.day == "Tuesday"])
print(data[data.day == "Saturday"])

# This code check for the highest temperature day in the week
print('\nThis code check for the highest temperature day in the week:')
print(data[data.temp == data.temp.max()])

# This print one tab at a time[Day, Temp, condition].
print('\nThis print one tab at a time.')
print( "print only the Day")
print(data.day)
print("print only the Temp")
print(data.temp)
print("print only the condition")
print(data.condition)














# '''Create a list of temperatures and then print them'''
# import csv
# with open('weather_data.csv') as weather_data:
#     data = csv.reader(weather_data)
#     for row in data:
#         print(row)
#
#
# '''Create a list of temperatures and then print them'''
# with open('weather_data.csv') as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

