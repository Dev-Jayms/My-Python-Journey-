# This input the reduce function from the functools module
from functools import reduce

'''
The reduce() function in Python is used to apply a function to the elements of an
iterable and reduce them to a single value. It takes a function as the first argument
and an iterable as the second argument. The function is applied to the
first two elements of the iterable, then the result is applied to the next element,
and so on until all elements have been processed.'''


def add(x, y):
    # Adds two numbers together and returns the result.
    return x + y


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# result = reduce(add, numbers)
# print(result)
print(reduce(add, numbers))
