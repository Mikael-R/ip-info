from requests import get
from sys import argv as argument
from subprocess import call

try:  # shell=True the command is executed on the terminal
    call('clear', shell=True)
except:
    call('cls', shell=True)

def connection():
    try:
        get(f'https://ipinfo.io')
        return True
    except:
        return False


def get_site_ip(site):
    try:
        from socket import gethostbyname as gethost
        print(f'* Site IP was found:\n  {gethost(site)}')
    except:
        print(f'* Site IP was not found.')
        exit()


def valid_ip(request):
    try:
        request.json()["ip"]
        return True
    except:
        return False

## MAIN ##
if connection() == False:
    print('* Could not establish a connection.')
    exit()

if len(argument) < 2:
    print('* Arguments not passed.')
    exit()

protocol = argument[1].lower()

if protocol == 'help':
    print(f'''
{'=' * 32}
* python3 main.py ip <ip>
* python3 main.py site <url>
{'=' * 32}
    ''')

elif protocol == 'site':
    get_site_ip(argument[2])

elif protocol == 'ip':

    IP = argument[2]

    request = get(f'https://ipinfo.io/{IP}')

    if valid_ip(request) == False:
        request = get(f'https://ipinfo.io')
        print ('* IP address not found.')

        use_local_ip = input('* Do you want to use your local ip address (y/n)? ').strip().lower()
        if use_local_ip == 'n':
            exit()

    IPInfoJSON = request.json()

    try:
        postal = IPInfoJSON["postal"]
    except:
        postal = 'undefined'

    print(f"""
{'='*43}
• IP: {IPInfoJSON["ip"]}
• City: {IPInfoJSON["city"]}
• Region: {IPInfoJSON["region"]}
• Country: {IPInfoJSON["country"]}
• Coordinates: {IPInfoJSON["loc"]}
• Postal Code: {postal}
• Timezone: {IPInfoJSON["timezone"]}
• Org: {IPInfoJSON["org"]}
{'='*43}
""")

else:
    print('* Invalid protocol.')
