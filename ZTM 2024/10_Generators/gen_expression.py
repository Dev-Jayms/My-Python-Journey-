# This is the code snippet for Generator expression
# (expression for item in iterable)

gen_exp = (i*i for i in range(1, 11))

print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
