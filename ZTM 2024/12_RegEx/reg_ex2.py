import re

# This regex searches for email address pattern
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email_add = "james@gmail.com"
print(pattern.search(email_add))
