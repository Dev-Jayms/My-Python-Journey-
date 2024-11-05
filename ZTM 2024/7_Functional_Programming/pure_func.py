"""
This function takes a list of numbers as input and returns a new list where each number is multiplied by 2.

Parameters:
    li (list): A list of numbers.

Returns:
    list: A new list where each number is multiplied by 2.
"""


def multiply_by2(li):
    new_list = []
    for num in li:
        new_list.append(num*2)

    return new_list


print(multiply_by2([15, 20, 30]))
