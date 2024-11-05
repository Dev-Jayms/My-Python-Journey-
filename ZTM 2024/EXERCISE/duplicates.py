# Check for duplicate in list
letters =                     ["a","b","c","b","d","m","n","n"]

duplicates = []
for value in letters:
    if letters.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

# def F(n):
#     if n <= 1:
#         return n
#     else:
#         return F(n - 1) + F(n - 2)

# print(F(15))