""" 
You're going to use Dictionary Comprehension to create a dictionary called "weather_f" that takes each
temperature in degrees Celcius and converts it into degrees Fahrenheit and then present the output
using pandas.
"""

import pandas as pd

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# Convert temperatures from Celcius to Fahrenheit
weather_f = {day: (temp * 9 / 5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

# Convert dictionary to DataFrame
df = pd.DataFrame(list(weather_f.items()), columns=["Day", "Temperature_F"])

# Save DataFrame to csv
df.to_csv("weather.csv", index=False)

print(df)
