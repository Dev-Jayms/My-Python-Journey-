import pandas as pd
# Create a dataframe from scratch with dictionary
data_dict = {
    "students": ["James","Binta","Rashida","Mohamed","Madiana"],
    "scores": [76,56,98,45,34]
}

data_frame = pd.DataFrame(data_dict)
print(data_frame)

# convert the dataframe to csv file
data_csv = data_frame.to_csv("new_data.csv")
