from requests import get


def IP_coerente(request):
    try:
        test = request.json()["ip"]
    except:
        return False
    else:
        return True


IP = input('\nIP: ')
r = get(f'http://ipinfo.io/{IP}')
if IP_coerente(request=r) == False:
    r = get(f'http://ipinfo.io')
    print('* Endereço IP informado não foi encontrado.')
    print('* Endereço IP local foi utilizado.')

IPInfoJSON = r.json()

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
