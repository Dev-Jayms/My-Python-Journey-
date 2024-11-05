# Genrator function
def gen():
    yield 1
    yield 2
    yield 3


# for _ in gen():
#     print(_)

# example 2


def gen2(num):
    for i in range(num):
        yield (i)

# x is a generator object
x = gen2(5)

# Iterating over the generator object using next
# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
