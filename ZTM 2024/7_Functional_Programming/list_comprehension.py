
'''This list comprehnsion is used to create a new list from an existing list 
in a shorter way
new_list = [expression for item in iterable]'''

my_list = [char for char in "hello"]
print('\nThis list comprehension is used to create a new list from an existing list in a shorter way')
print(my_list)

'''This list comprehension is used to find the even numbers in a shorter way'''
my_list2 = [num for num in range(1, 101) if num % 2 == 0]
print('\nThis list comprehension is used to find the even numbers in a shorter way')
print(my_list2)

'''This list comprehension is used to multiply the numbers by 2 from 1 - 100'''
my_list3 = [num*2 for num in range(1, 101)]
print('\nThis list comprehension is used to multiply the numbers by 2 from 1 - 100.')
print(my_list3)

# \This list comprehension is used to find the numbers that are divisible by 5 and 3.
my_list4 = [num for num in range(1, 1001) if num % 5 == 0 and num % 3 == 0]
print("\nThis list comprehension is used to find the numbers that are divisible by 5 and 3.")
print(my_list4)

my_list5 = [num**2 for num in range(1, 100) if num % 2 == 0]
print("\nThis list comprehension is used to multiply the square numbers by 2 from 1 - 100.")
print(my_list5)


# def my_list5(num):
#     for num in range(1, num):
#         if num % 2 == 0:
#             print(num**2)


# my_list5(100)
