'''
filter() function
The filter() function in Python is used to create an iterator that filters elements from an iterable 
based on a specified condition.
This function code generate an even number'''


def even_number(num):
    return num % 2 == 0


num_range = range(1, 51)

print("These are the Even Numbers:")
print(list(filter(even_number, num_range)))

'''
    This function code generate an odd number'''


def odd_number(num):
    return num % 2 != 0


num_range = range(1, 51)

print("\nThese are the Odd Numbers:")
print(list(filter(odd_number, num_range)))


'''This function code generate the names starting with J'''


def check_name(names):
    # Check if the first character of the given string is equal to "Z".
    return names[0] == "J"


# This list contains names to filter.
# names_list = ['James', 'Bill', 'Zane', 'Jack']
names_list = input("Enter names: ").upper().split(",")

print("\nThese are the names starting with J:")
print(list(filter(check_name, names_list)))
print("Number of names: ", len(names_list))
