simple_dict = {
    'a': 1,
    'b': 2}
'''Multiply the value of the simple_dict by 4'''
my_dict = {key: value*4 for key, value in simple_dict.items()}

print(my_dict)
