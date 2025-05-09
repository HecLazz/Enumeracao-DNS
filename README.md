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

## Atualizações

- Hector Lazzari
- 06/05/2025
- Adicionei a função Whois, que utiliza do "whois.iana.org", primeiro faz uma verificação da referência de onde está sendo pesquisado, por exemplo vou colocar "google.com", vai aparecer que a informação foi extraída de "whois.verisign-grs.com", após isso faz mais um filtro que vai pegar do "Registrar WHOIS Server:", tudo isso para caso algum desses link mude, não precise alterar o código.
- Estou começando construir um menu "dnsmenu.py"
- Tive um problema para ler o arquivo onde tem todos os subdominios, quando clonei o respositório, colocar apenas o nome do arquivo estava gerando um erro de arquivo não encontrado, mesmo estando na mesma pasta. Então coloquei o caminho absoluto (está comentado onde é para colocar o caminho do arquivo).
<br>
- Hector Lazzari
- 08/05/2025
- Consegui terminar partes do menu, como listagem de arquivos dentro de diretórios, executar a leitura do arquivo que você selecionar.
- Integrei melhor dentro do arquivo principal, tive a idéia de passar como parâmetro o dominio digitado direto para o menu, onde ficou muito melhor para manipular.
- Estou na dúvida se arquivo de texto é a melhor opção para salvar os resultados.