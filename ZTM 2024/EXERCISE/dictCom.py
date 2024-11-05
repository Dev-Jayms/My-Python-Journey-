"""
You're going to use a dictionary comprehension to create a dictionary  called "result" that takes each
words in the given sentence and calculate the number of letters in each word.
"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?".split()
result = {word: len(word) for word in sentence}
print(result)

# for word in sentence:
#     print(word, len(word))
