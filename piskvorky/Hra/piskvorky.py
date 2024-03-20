from tkinter import *
import random

# Globální proměnné
hráči = ["X", "O"]
hráč = random.choice(hráči)
tlačítka = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
kola = {hráči[0]: 0, hráči[1]: 0}
celková_kola = 3
odehraná_kola = 0
pauza_kola = False

# Funkce pro kontrolu prázdných polí na hrací desce
def prázdná_pole():
    počet_prázdných = 25
    for řádek in range(5):
        for sloupec in range(5):
            if tlačítka[řádek][sloupec]['text'] != "":
                počet_prázdných -= 1
    return počet_prázdných > 0
