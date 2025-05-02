import socket
import dns.resolver
from concurrent.futures import ThreadPoolExecutor

help = """
    [help]
    -c = cname
    -d = dns resolver
"""
print(help)
tipo = input("Escolha o tipo: ")
dominio = input("Digite o dominio: ")

def Dns(dominio_completo):
    try:
        dns = socket.getaddrinfo(dominio_completo, 43, family=socket.AF_INET, proto=socket.IPPROTO_TCP)
        addr = dns[0][4][0]
        print(f"{dominio_completo} - {addr}")

        with open(f"resultado-{dominio}.txt", "a") as save:
            save.write(f"{dominio_completo} - {addr}\n")
        return addr
    except socket.gaierror:
        return None

def Cname(dominio_completo):
    resposta = dns.resolver.resolve(dominio_completo, "CNAME")
    
    for i in resposta:
        print(f"{dominio_completo} - {i.target}")
        with open(f"resultado-cname-{dominio}.txt", "a") as save:
            save.write(f"{dominio_completo} - {i.target}\n")
    return resposta


with open("subdomains-10000.txt", "r") as sub:
    subdominio = [linha.strip() for linha in sub.readlines()]
        
with ThreadPoolExecutor(max_workers=100) as exe:
    if tipo == "-d":
        futures = [
            exe.submit(Dns, f"{sub}.{dominio}" )
            for sub in subdominio
        ]
    elif tipo == "-c":
        futures = [
            exe.submit(Cname, f"{sub}.{dominio}")
            for sub in subdominio
        ]
