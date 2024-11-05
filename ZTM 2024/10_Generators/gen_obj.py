# A Python program to demonstrate use of generator object with next()

# A generator function
def genObj():
    yield 1
    yield 2
    yield 3

# x is a generator object
x = genObj()
# Iterating over the generator object using next
# print(next(x))
# print(next(x))
# print(next(x))

# Iterating over the generator object using forloop
for items in x:
    print(items)
