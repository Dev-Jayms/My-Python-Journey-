"""Examples of list comprehension"""

# list comprehension with numbers.
numbers = [1, 2, 3 ]
new_numbers = [num + 1 for num in numbers]
print(new_numbers)

# list comprehension with letters.
letters = "James"
new_letters = [letter for letter in letters]
print(new_letters)

# list comprehension with numbers range.
new_range = [num * 2 for num in range(1, 5)]
print(new_range)


# List comprehension with expression
# This return the names that are four letter words.
names = ["James", "Alex", "Jamestina", "Beth", "Dave", "Madiana", "Caroline"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# Thia code names that are longer than 5 letters word and in uppercase
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)