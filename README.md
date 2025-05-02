# Projeto: DNS Enumerator
Um scanner para mapear subdomínios e registro CNAME. O projeto testa uma lista de subdomínios (ex.: sudmonais-10000.txt) em paralelo, indentificando:
- Endereços IP - consulta DNS padrão com socket.getaddrinfo.
- Registros CNAME - apelidos que redirecionam para outros domínios, usando dnspython.

## Funcionalidades 
- Varredura em massa com threads (100+ subdomínios simultâneos)
- Saída em arquivo (resultado-[dominio].txt e resultado-cname-[dominio].txt).

## Tecnologias
- Python 3
- Bibliotecas socket, dnspython, concurrent.futures
