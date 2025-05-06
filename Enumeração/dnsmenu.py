import os

class Menu:
    def __init__(self, dominio):
        
        if os.path.exists("scans") == False:
            os.mkdir("scans")

        if os.path.exists(f"scans/{dominio}") == False:
            os.mkdir(f"scans/{dominio}")