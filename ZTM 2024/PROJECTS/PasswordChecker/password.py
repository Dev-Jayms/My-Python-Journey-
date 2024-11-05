import requests
import hashlib


# def request_api_data(query_char):
#     url = "https://api.pwnedpasswords.com/range/" + query_char
#     res = requests.get(url)
#     if res.status_code != 200:
#         raise RuntimeError(f"error fetching: {
#                            res.status_code}, check the api and try again.")
#     return res


# def pwned_api_check(password):
#     # check password if it exist in API response
#     sha1password = hashlib.sha1(password.encode("utf=8")).hexdigest().upper()
#     first5_char, tail = sha1password[:5], sha1password[5:]
#     response = request_api_data(first5_char)
#     print(response)
#     return response

# creating a password generating app to check for if the password has been leaked in any of the sites.


'''
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


password = generate_password(12)
print(password)

'''


def check_password(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code == 200:
        for line in response.text.splitlines():
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return True
    return False


password = "mypassword123"
is_leaked = check_password(password)
print(is_leaked)
