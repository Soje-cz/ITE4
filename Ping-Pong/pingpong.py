#kod na ping pong do programovani (projekt)
#Jan Navrátil, Andrea Smílková


#import vsech veci
import random
import pyglet
from pyglet import gl
from pyglet.window import key


#zadani si zakladnich parametru
SIRKA = 900
VYSKA = 600

VELIKOST_MICE = 20
TLOUSTKA_PALKY = 10
DELKA_PALKY = 100
RYCHLOST = 200
RYCHLOST_PALKY = RYCHLOST * 1.5

DELKA_PULICI_CARKY = 20
VELIKOST_FONTU = 42
ODSAZENI_TEXTU = 100

pozice_palek = [SIRKA // 2, SIRKA // 2]
pozice_mice = [0, 0]
rychlost_mice = [0, 0]
stisknute_klavesy = set()
skore = [0, 0]