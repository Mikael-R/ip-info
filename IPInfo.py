from requests import get


def internet():
    try:
        get(f'https://ipinfo.io')
        return True
    except:
        return False


def IP_site(site):
    try:
        from socket import gethostbyname as gethost
        print(f'* IP do site foi encontrado:\n  {gethost(site)}')
    except:
        print(f'* IP do site não foi encontrado.')
        exit()


def IP_coerente(request):
    try:
        request.json()["ip"]
        return True
    except:
        return False


if internet() == False:
    print('* Não foi possível estabelecer uma conexão.')
    exit()


if internet == False:
    print('* Não foi possível estabelecer uma conexão.')
    exit()

protocolo = input('\nIP/Site: ').strip().lower()

if protocolo == 'site':
    print('''
Exemplo: www.google.com
         google.com
''')
    site = input('\nSite: ').strip()
    IP_site(site)

if protocolo == 'ip':
    print('''
Exemplo: XXX.XXX.XX.XXX
         XXX.XXX.X.X
''')
    IP = input('IP: ').strip()

    request = get(f'https://ipinfo.io/{IP}')

    if IP_coerente(request) == False:
        request = get(f'https://ipinfo.io')
        print('* Endereço IP não encontrado.')
        print('* Endereço IP local utilizado.')

    IPInfoJSON = request.json()

    IP = IPInfoJSON["ip"]
    cidade = IPInfoJSON["city"]
    regiao = IPInfoJSON["region"]
    territorio = IPInfoJSON["country"]
    coordenadas = IPInfoJSON["loc"]
    CEP = IPInfoJSON["postal"]
    fuso_horario = IPInfoJSON["timezone"]
    provedor = IPInfoJSON["org"]

    print(f"""
{'='*43}
• IP: {IP}
• Cidade: {cidade}
• Estado: {regiao}
• País: {territorio}
• Coordenadas: {coordenadas}
• CEP: {CEP}
• Fuso horário: {fuso_horario}
• Provedor: {provedor}
{'='*43}
""")
