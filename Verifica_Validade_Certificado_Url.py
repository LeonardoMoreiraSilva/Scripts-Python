import ssl
import socket
import datetime

def get_certificate_expiry_date(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            not_after = cert['notAfter']
            expiry_date = datetime.datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
            return expiry_date

# Arquivo contendo as URLs (uma URL por linha)
url_file = "/home/leonardo/ScriptsVia/PegaDataCertificadoURL_VIA/urls"

# Ler as URLs do arquivo
with open(url_file, 'r') as file:
    lines = file.readlines()

current_product = None

# Validar cada URL
for line in lines:
    line = line.strip()
    if line.startswith("#"):
        current_product = line.strip("# ")
        print()
        print(f"Produto: {current_product}")
        continue

    if line:
        url = line
        expiry_date = get_certificate_expiry_date(url)
        expiry_date_formatted = expiry_date.strftime("%d-%m-%Y %H:%M:%S")
        print(f"Url: {url} ")
        print(f"Valido: {expiry_date_formatted}")
#        print()  # Linha em branco para separar as saídas
