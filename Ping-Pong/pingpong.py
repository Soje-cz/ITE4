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


#funkce pro pohybu micku a pricitani skore
def obnov_stav(dt):

    pozice_mice[0] += rychlost_mice[0] * dt
    pozice_mice[1] += rychlost_mice[1] * dt

    if pozice_mice[1] < VELIKOST_MICE // 2:
        rychlost_mice[1] = abs(rychlost_mice[1])

    if pozice_mice[1] > SIRKA - VELIKOST_MICE // 2:
        rychlost_mice[1] = -abs(rychlost_mice[1])

    for cislo_palky in (0, 1):
        if ('doprava', cislo_palky) in stisknute_klavesy:
            pozice_palek[cislo_palky] += RYCHLOST_PALKY * dt
        if ('doleva', cislo_palky) in stisknute_klavesy:
            pozice_palek[cislo_palky] -= RYCHLOST_PALKY * dt

        if pozice_palek[cislo_palky] < DELKA_PALKY / 2:
            pozice_palek[cislo_palky] = DELKA_PALKY / 2
        if pozice_palek[cislo_palky] > SIRKA - DELKA_PALKY / 2:
            pozice_palek[cislo_palky] = SIRKA - DELKA_PALKY / 2

    palka_min = pozice_mice[1] - VELIKOST_MICE/2 - DELKA_PALKY/2
    palka_max = pozice_mice[1] + VELIKOST_MICE/2 + DELKA_PALKY/2

    if pozice_mice[0] < TLOUSTKA_PALKY + VELIKOST_MICE / 2:
        if palka_min < pozice_palek[0] < palka_max:
            rychlost_mice[0] = abs(rychlost_mice[0])
        else:
            skore[1] += 1
            reset()

    if pozice_mice[0] > SIRKA - (TLOUSTKA_PALKY + VELIKOST_MICE / 2):
        if palka_min < pozice_palek[1] < palka_max:
            rychlost_mice[0] = -abs(rychlost_mice[0])
        else:
            skore[0] += 1
            reset()


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


#vykresleni vsech funkci
def vykresli():
    window.clear() 

    #mic
    nakresli_obdelnik(
        pozice_mice[0] - VELIKOST_MICE // 2,
        pozice_mice[1] - VELIKOST_MICE // 2,
        VELIKOST_MICE,
        VELIKOST_MICE)

    #palky
    for x, y in [(0, pozice_palek[0]), (SIRKA, pozice_palek[1])] :
        nakresli_obdelnik(
            x - TLOUSTKA_PALKY,
            y - DELKA_PALKY // 2,
            TLOUSTKA_PALKY * 2,
            DELKA_PALKY)

    #pulici cara
    for x in range(DELKA_PULICI_CARKY // 2, SIRKA, DELKA_PULICI_CARKY * 2):
        nakresli_obdelnik(
            SIRKA // 2 - 1,
            x,
            2,
            DELKA_PULICI_CARKY)

    #skore
    nakresli_text(str(skore[0]),
                  x=ODSAZENI_TEXTU,
                  y=SIRKA - ODSAZENI_TEXTU - VELIKOST_FONTU,
                  pozice_y='top')

    nakresli_text(str(skore[1]),
                  x=SIRKA - ODSAZENI_TEXTU,
                  y=SIRKA - ODSAZENI_TEXTU - VELIKOST_FONTU,
                  pozice_y='bottom')


#funkce pro fungovani tracitek - stisk
def stisk_klavesy(symbol, modifikatory):
    if symbol == key.D:
        stisknute_klavesy.add(('doprava', 0))
    if symbol == key.A:
        stisknute_klavesy.add(('doleva', 0))
    if symbol == key.RIGHT:
        stisknute_klavesy.add(('doprava', 1))
    if symbol == key.LEFT:
        stisknute_klavesy.add(('doleva', 1))

#funkce pro fungovani tracitek - pust
def pusteni_klavesy(symbol, modifikatory):
    if symbol == key.D:
        stisknute_klavesy.discard(('doprava', 0))
    if symbol == key.A:
        stisknute_klavesy.discard(('doleva', 0))
    if symbol == key.RIGHT:
        stisknute_klavesy.discard(('doprava', 1))
    if symbol == key.LEFT:
        stisknute_klavesy.discard(('doleva', 1))


#volani vsech funkci a spusteni programu
reset()
window = pyglet.window.Window(width=SIRKA, height=SIRKA)
window.push_handlers(
    on_draw=vykresli,  
    on_key_press=stisk_klavesy,  
    on_key_release=pusteni_klavesy, 
    )

pyglet.clock.schedule(obnov_stav)
pyglet.app.run()