"""
In Python, a lambda function is a small anonymous function that can be defined
without a name. It is typically used when you need a simple function that is only used 
once or in a specific context. The syntax for a lambda function is as follows:

lambda arguments: expression"""
# A lambda function that adds two numbers
add = [3, 4]
result = list(map(lambda x: x[0] + x[1], zip(add, add)))
print(result)

'''
In this example, we use a lambda function as an argument to the map() function.
The lambda function takes an element x from the numbers list and returns its square.
The map() function applies this lambda function to each element in the numbers list,
and the result is a new list of squared numbers
'''
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
