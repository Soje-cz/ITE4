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
def vymazat_desku():
    for řádek in range(5):
        for sloupec in range(5):
            tlačítka[řádek][sloupec].config(text="", bg="#FFFFFF")  # Změna pozadí na bílé pro lepší čitelnost

# Funkce pro aktualizaci počtu odehraných kol
def aktualizovat_kola():
    popisky_kol.config(text="Kola: " + str(kola[hráči[0]]) + " - " + str(kola[hráči[1]]))

# Funkce pro zakázání tlačítek na konci hry
def zakázat_tlačítka():
    for řádek in range(5):
        for sloupec in range(5):
            tlačítka[řádek][sloupec].config(state="disabled")
            tlačítka[řádek][sloupec].config(bg="#FFFFFF")  # Změna pozadí na bílé pro lepší čitelnost

# Funkce pro povolení tlačítek pro nové kolo
def povolit_tlačítka():
    for řádek in range(5):
        for sloupec in range(5):
            tlačítka[řádek][sloupec].config(state="normal")
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

# Funkce pro spuštění nového kola
def nové_kolo():
    global hráč, pauza_kola

    hráč = random.choice(hráči)
    popisek.config(text=hráč
 + " je na tahu")
    vymazat_desku()
    povolit_tlačítka()
    pauza_kola = False

# Funkce pro zvýraznění vítězné linie
def zdůraznit_výherní():
    for řádek in range(5):
        for sloupec in range(5):
            tlačítka[řádek][sloupec].config(state="disabled")
    kontrola_výhry()  # Zvýraznit vítěznou linii

# Funkce pro spuštění nové hry
def nová_hra():
    global hráč, kola, odehraná_kola, pauza_kola
    hráč = random.choice(hráči)
    kola = {hráči[0]: 0, hráči[1]: 0}
    odehraná_kola = 0
    popisek.config(text=hráč + " je na tahu")
    popisky_kol.config(text="Kola: 0 - 0")
    vymazat_desku()
    povolit_tlačítka()
    pauza_kola = False
    tlačítko_kola.config(state="normal")  # Povolit tlačítko pro nové kolo
okno = Tk()
okno.title("Piškvorky")

# Nastavení fontů popisků pro lepší čitelnost
popisek = Label(text=hráč + " je na tahu", font=('Arial', 18, 'bold'))
popisek.pack(side="top")

popisky_kol = Label(text="Kola: 0 - 0", font=('Arial', 14))
popisky_kol.pack(side="top")

tlačítko_restart = Button(text="Restart", font=('Arial', 14), command=nová_hra)
tlačítko_restart.pack(side="top")

tlačítko_kola = Button(text="Nové kolo", font=('Arial', 14), command=nové_kolo)
tlačítko_kola.pack(side="top")

rámec = Frame(okno)
rámec.pack()

# Přizpůsobení vzhledu tlačítek pro čistší vzhled
for řádek in range(5):
    for sloupec in range(5):
        tlačítka[řádek][sloupec] = Button(rámec, text="", font=('Arial', 20), width=3, height=1,
                                           command=lambda řádek=řádek, sloupec=sloupec: další_kolo(řádek, sloupec))
        tlačítka[řádek][sloupec].grid(row=řádek, column=sloupec, padx=2, pady=2)  # Přidání odsazení pro lepší rozestup

okno.mainloop()

