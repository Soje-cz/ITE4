#kod na ping pong do programovani (projekt)
#Jan Navrátil, Andrea Smílková, David Koukol


#import vsech veci
import random
import pyglet
from pyglet import gl
from pyglet.window import key


#zadani si zakladnich parametru

#rozmery okna
SIRKA = 900
VYSKA = 600

#rozmery mince, palky a rychlost
VELIKOST_MICE = 20
TLOUSTKA_PALKY = 10
DELKA_PALKY = 100
RYCHLOST = 200
RYCHLOST_PALKY = RYCHLOST * 1.5

#rozmery pulici cary a velikost textu
DELKA_PULICI_CARKY = 20
VELIKOST_FONTU = 42
ODSAZENI_TEXTU = 100

#nastaveni pozice vseho, pridani skore a ovladani pomoci klavesnice
pozice_palek = [SIRKA // 2, SIRKA // 2]
pozice_mice = [0, 0]
rychlost_mice = [0, 0]
stisknute_klavesy = set()
skore = [0, 0]

#definovani vsech funkci

#funkce pro resetovani micku
def reset():

    pozice_mice[0] = SIRKA // 2
    pozice_mice[1] = VYSKA // 2

    if random.randint(0, 1):
        rychlost_mice[0] = RYCHLOST
    else:
        rychlost_mice[0] = -RYCHLOST
    rychlost_mice[1] = random.uniform(-1, 1) * RYCHLOST


#funkce pro kresleni palek, micku
def nakresli_obdelnik(x, y, sirka, vyska):
    obdelnik = pyglet.shapes.Rectangle(x=y, y=x, width=vyska, height=sirka)
    obdelnik.draw()

#funkce pro kreselni skore
def nakresli_text(text, x, y, pozice_y):
    napis = pyglet.text.Label(
        text,
        font_size=VELIKOST_FONTU,
        x=y, y=x, anchor_y=pozice_y)
    napis.draw()