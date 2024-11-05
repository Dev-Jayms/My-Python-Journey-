'''
MAP() Function

The map() function in Python is used to apply a function to each item in an iterable 
(such as a list, tuple, or string) and return a new iterable with the results.

'''

my_list = [123]


def multiply_by3(num):
    return num*3


# The map() function returns an object that can be converted into a list.
print(list(map(multiply_by3, my_list)))
# The map() function doesn'africa affect the original username variable.
print(my_list)


'''This code return a name in upper case within a list'''


def greeting(name):
    return name.upper()


username = input("What's your name? ")
# The map() function returns an object that can be converted into a list.
print(list(map(greeting, username)))
# The map() function doesn'africa affect the original username variable.
print(username)
