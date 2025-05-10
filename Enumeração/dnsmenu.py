import os

class Menu:
    def __init__(self, dominio):
        
        if os.path.exists("scans") == False:
            os.mkdir("scans")

        if os.path.exists(f"scans/{dominio}") == False:
            os.mkdir(f"scans/{dominio}")
            
    def menu(dominio):
        try:
            id = 0
            scans = os.listdir(f"scans/{dominio}")

            print("==============================\n")
            for i in scans:
                print(f"{id} - {i}")
                id += 1

            print("\nEscolha o ID do arquivo\n")
            arquivo = int(input("> "))

            caminho_arquivo = scans[arquivo]
            print(caminho_arquivo)
            with open(f"scans/{dominio}/{caminho_arquivo}", "r") as f:
                tipo = f.read()
            print(tipo)
        except FileNotFoundError:
            print("\nArquivo não foi gerado!\n")
