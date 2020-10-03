import requests
import socket
import time

DOMAIN        = "myurl.tld" # Domain name without prefix or http
DOMAIN_PREFIX = "prefix" # Domain name prefix (full url would be prefix.myurl.tld)
PASSWORD      = "1273abcdef69420aaaaaaaaaaaaaaaaa" # Namecheap ddns password
LOOP_TIME     = 600 #Time before each ip update in milliseconds

p_ip = socket.gethostbyname(f'{DOMAIN_PREFIX}.{DOMAIN}')

def update(ip):
    requests.get(f'https://dynamicdns.park-your-domain.com/update?host={DOMAIN_PREFIX}&domain={DOMAIN}&password={PASSWORD}&ip={ip}')
    print(f'IP UPDATED: {ip}')

while True:
    n_ip = requests.get("http://icanhazip.com/").text.strip("\n")
    if n_ip != p_ip:
        p_ip = n_ip
        update(n_ip)
    time.sleep(LOOP_TIME)