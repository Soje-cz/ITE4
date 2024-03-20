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

def kontrola_výhry():
    for řádek in range(5):
        if tlačítka[řádek][0]['text'] == tlačítka[řádek][1]['text'] == tlačítka[řádek][2]['text'] == tlačítka[řádek][3]['text'] != "":
            for i in range(5):
                tlačítka[řádek][i].config(bg="green")
            return True
    for sloupec in range(5):
        if tlačítka[0][sloupec]['text'] == tlačítka[1][sloupec]['text'] == tlačítka[2][sloupec]['text'] == tlačítka[3][sloupec]['text'] != "":
            for i in range(5):
                tlačítka[i][sloupec].config(bg="green")
            return True
    if tlačítka[0][0]['text'] == tlačítka[1][1]['text'] == tlačítka[2][2]['text'] == tlačítka[3][3]['text'] != "":
        for i in range(5):
            tlačítka[i][i].config(bg="green")
        return True
    elif tlačítka[0][4]['text'] == tlačítka[1][3]['text'] == tlačítka[2][2]['text'] == tlačítka[3][1]['text'] != "":
        for i in range(5):
            tlačítka[i][4-i].config(bg="green")
        return True
    elif prázdná_pole() is False:
        for řádek in range(5):
            for sloupec in range(5):
                tlačítka[řádek][sloupec].config(bg="yellow")
        return "Remíza"
    else:
        return False

# Funkce pro další tah
def další_kolo(řádek, sloupec):
    global hráč, odehraná_kola, pauza_kola
    if tlačítka[řádek][sloupec]['text'] == "" and kontrola_výhry() is False and not pauza_kola:
        tlačítka[řádek][sloupec]['text'] = hráč

        if kontrola_výhry() is True:
            kola[hráč] += 1
            aktualizovat_kola()

            if kola[hráč] == celková_kola:
                popisek.config(text=hráč + " vyhrál hru!")
                zakázat_tlačítka()
                pauza_kola = True
                odehraná_kola += 1
                tlačítko_kola.config(state="disabled")  # Zakázat tlačítko pro nové kolo
            else:
                popisek.config(text=hráč + " vyhrál kolo!")
                vymazat_desku()
                aktualizovat_kola()
                zdůraznit_výherní()
                pauza_kola = True
                odehraná_kola += 1
        elif kontrola_výhry() == "Remíza":
            popisek.config(text="Remíza!")
            vymazat_desku()
            aktualizovat_kola()
            pauza_kola = True
            odehraná_kola += 1
        else:
            hráč = hráči[1] if hráč == hráči[0] else hráči[0]
            popisek.config(text=(hráč + " je na tahu"))

