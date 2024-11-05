'''
zip() function
The zip() function in Python is used to combine multiple iterables into a single iterable of tuples,
where each tuple contains the corresponding elements from each iterable.

This code takes two or more variables that are iterable and adds them to a list of tuples'''
first_name = input("What's your first name? ").upper().split(",")
last_name = input("What's your last name? ").upper().split(",")


print(list(zip(first_name, last_name, )))
