# A simple generator for Fibonacci Numbers

def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a  # One by one yield next Fibonacci Number
        c = a
        a = b
        b += c


# iterating over the fibonnaci function using forloop.
for i in fib(21):
    print(i)


# Create a generator object
# x = fib(1, 22)
# print(next(x))
# print(next(x))
# print(next(x))
