"""
Create a list of numbers which are common in both file1 and file2 and output them in result.
"""
with open("file1.txt") as file1:
    file_1_data = file1.readlines()
    
with open("file2.txt", encoding = "utf8") as file2:
    file_2_data = file2.readlines()
    
result = [int(num) for num in file_1_data if num in file_2_data ]
print(result)

# import os

# print(os.getcwd())