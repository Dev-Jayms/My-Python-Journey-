# This import the regular expression module.
import re

string = "My name is James"
result = re.search("James", string)
print(result)
print(result.start())  # This print the index where the search word start
print(result.end())  # This print the index where the search word end
print(result.span())  # This print the index where the search word start and end
print(result.string)  # This print the entire sentence
