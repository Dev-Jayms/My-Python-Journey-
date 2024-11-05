"""
Convert degrees Fahrenheit and converts it into degrees Celcius and then present the output
using pandas."""

import pandas as pd


# Data in Fahrenheit
data = {
    "Day": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ],
    "Temperature_F": [53.6, 57.2, 59.0, 57.2, 69.8, 71.6, 75.2],
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Fahrenheit to Celsius
df["Temperature_C"] = (df["Temperature_F"] - 32) * 5 / 9

# Save to CSV
df.to_csv("weather_celsius.csv", index=False)

print(df)
