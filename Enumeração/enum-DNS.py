import socket
import dns.resolver
import dnsmenu
from concurrent.futures import ThreadPoolExecutor

menu = dnsmenu.Menu

help = """
    [help]
    -c = cname
    -d = dns resolver
    -w = whois
"""
print(help)
tipo = input("Escolha o tipo: ")
dominio = input("Digite o dominio: ")

menu(dominio)

def Dns(dominio_completo):
    try:
        dns = socket.getaddrinfo(dominio_completo, 43, family=socket.AF_INET, proto=socket.IPPROTO_TCP)
        addr = dns[0][4][0]
        print(f"{dominio_completo} - {addr}")

        with open(f"scans/{dominio}/resultado-{dominio}.txt", "a") as save:
            save.write(f"{dominio_completo} - {addr}\n")
        return addr
    except socket.gaierror:
        return None

def Cname(dominio_completo):
    resposta = dns.resolver.resolve(dominio_completo, "CNAME")
    
    for i in resposta:
        print(f"{dominio_completo} - {i.target}")
        with open(f"scans/{dominio}/resultado-cname-{dominio}.txt", "a") as save:
            save.write(f"{dominio_completo} - {i.target}\n")
    return resposta

def Whois(dominio):
    d = dominio + "\r\n"
    def Opensocket(dominio, d):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((dominio, 43))
        s.send((d.encode()))
        return s

    if ".br" in dominio:
        s = Opensocket("whois.iana.org", d)
        whois1 = s.recv(1024).decode().split("refer:        ")[1].split("\n\n")[0]
        s.close()

        s = Opensocket(whois1, d)
        resultado_br = ""
        while True:
            data_br = s.recv(8040)
            if data_br:
                resultado_br += data_br.decode()
            else:
                break 

            with open(f"scans/{dominio}/{dominio}.whois.txt", "w") as f:
                f.write(resultado_br)
        s.close()
    else:
        s = Opensocket("whois.iana.org", d)
        whois1 = s.recv(1024).decode().split("refer:        ")[1].split("\n\n")[0]
        s.close()

        s = Opensocket(whois1, d)
        whois2 = s.recv(1024).decode().split("Registrar WHOIS Server: ")[1].split("\r\n")[0]
        s.close()

        s = Opensocket(whois2, d)
        resultado = ""
        while True:
            data = s.recv(8040)
            if data: 
                resultado += data.decode()
            else:
                break 

            with open(f"scans/{dominio}/{dominio}.whois.txt", "w") as f:
                f.write(resultado)
        s.close()
    return 0

# Aqui coloque o caminho absoluto do arquivo "subdomains-10000.txt"
with open("/home/kali/Documents/Enumeracao-DNS/Enumeração/subdomains-10000.txt", "r") as sub:
    subdominio = [linha.strip() for linha in sub.readlines()]
        
with ThreadPoolExecutor(max_workers=100) as exe:
    if tipo == "-d":
        futures = [
            exe.submit(Dns, f"{sub}.{dominio}")
            for sub in subdominio
        ]
    elif tipo == "-c":
        futures = [
            exe.submit(Cname, f"{sub}.{dominio}")
            for sub in subdominio
        ]
    elif tipo == "-w":
        Whois(dominio)
