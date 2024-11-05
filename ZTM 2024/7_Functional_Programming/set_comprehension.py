
'''This set comprehnsion is used to create a new list from an existing set in a shorter way'''
my_set = {char for char in "hello"}
print('\nThis list comprehension is used to create a new list from an existing set in a shorter way')
print(my_set)

'''This list comprehension is used to find the even numbers in a shorter way'''
my_set2 = {num for num in range(1, 101) if num % 2 == 0}
print('\nThis list comprehension is used to find the even numbers in a shorter way')
print(my_set2)

'''This set comprehension is used to multiply the numbers by 2 from 1 - 100'''
my_set3 = {num*2 for num in range(1, 101)}
print('\nThis set comprehension is used to multiply the numbers by 2 from 1 - 100.')
print(my_set3)
