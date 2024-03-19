import random
import msvcrt

print("Vítejte v Casinu imperial")

global konto

konto = 0

# Barvy textu
def print_red(text):
    print("\033[91m{}\033[00m".format(text))  # Red text
def print_green(text):
    print("\033[92m{}\033[00m".format(text))  # Green text
def print_yellow(text):
    print("\033[93m{}\033[00m".format(text))  # Yellow text
def print_magenta(text):
    print("\033[95m{}\033[00m".format(text))  # Magenta text
def print_cyan(text):
    print("\033[96m{}\033[00m".format(text))  # Cyan text
def print_pink(text):
    print("\033[94m{}\033[00m".format(text))
def penize():
    global konto
    if konto >= 0:
        print_yellow("Na vašem kontě je " + str(konto))
        choice = input("Chcete vložit finanční prostředky? (ano/ne): ")
        if choice == "ano":
            add_konto = int(input("Zadejte čásku: "))
            konto = konto + add_konto
            print_yellow("Na vašem kontě máte "+ str(konto) +" korun.")
            casino()
        elif choice == "ne":
            casino()
        else:
            print("Toto nebyla možnost.")
            penize()
def sazka():
    




def rulleta():
    global konto
    while True:
        bet = int(input("Zadejte sázku prosím: "))
        if bet > konto:
            print("Nemáte dostatek financí.")
            continue
        if bet <= konto:
            break

    Black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    Red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    Even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
    Odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]

    print_magenta("Na co chcete vsadit:")
    print_cyan("1. Červená")
    print_pink("2. Černá")
    print_cyan("3. Sudá")
    print_pink("4. Lichá")
    print_cyan("5. Číslo")

    choice = input("Vyberte operaci (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        roll = random.randint(0, 36)
        if choice == '1':
            if roll in Red:
                konto = konto - bet + bet * 2
                print_green("Výhra!")
            else:
                konto -= bet
                print_red("Prohra.")
        elif choice == '2':
            if roll in Black:
                konto = konto - bet + bet * 2
                print_green("Výhra!")
            else:
                konto -= bet
                print_red("Prohra.")
        elif choice == '3':
            if roll in Even:
                konto = konto - bet + bet * 2
                print_green("Výhra!")
            else:
                konto -= bet
                print_red("Prohra.")
        elif choice == '4':
            if roll in Odd:
                konto = konto - bet + bet * 2
                print_green("Výhra!")
            else:
                konto -= bet
                print_red("Prohra.")
        elif choice == '5':
            cislo = int(input("Zadejte číslo na které chcete vsadit: "))
            if roll == cislo:
                konto = konto - bet + bet * 5
                print_green("Výhra!")
            else:
                konto -= bet
                print_red("Prohra.")

        print("Padlo číslo:", roll)
        print_yellow("Stav konta: "+ str(konto))

        if konto == 0:
            print_yellow("Došly vám peníze.")
            return False
        return True

def Blackjack():
    global konto
    while True:
        bet = int(input("Zadejte sázku prosím: "))
        if bet > konto:
            print_yellow("Nemáte dostatek financí.")
            continue
        if bet <= konto:
            break

    # Baliček karet
    deck = ["Eso ♠", "2 ♠", "3 ♠", "4 ♠", "5 ♠", "6 ♠", "7 ♠", "8 ♠", "9 ♠", "10 ♠", "Jack ♠", "Dama ♠", "Kral ♠", 
            "Eso ♣", "2 ♣", "3 ♣", "4 ♣", "5 ♣", "6 ♣", "7 ♣", "8 ♣", "9 ♣", "10 ♣", "Jack ♣", "Dama ♣", "Kral ♣", 
            "Eso ♥", "2 ♥", "3 ♥", "4 ♥", "5 ♥", "6 ♥", "7 ♥", "8 ♥", "9 ♥", "10 ♥", "Jack ♥", "Dama ♥", "Kral ♥",
            "Eso ♦", "2 ♦", "3 ♦", "4 ♦", "5 ♦", "6 ♦", "7 ♦", "8 ♦", "9 ♦", "10 ♦", "Jack ♦", "Dama ♦", "Kral ♦"]

    # Zamichani baličku
    random.shuffle(deck)

    # Karty hráče
    player_hand = []

    # Karty dealera
    dealer_hand = []

    # Rozdá první dve karty hraci
    for i in range(2):
        player_hand.append(deck.pop(0))

    # Rozdá první dve karty dealerovi
    for i in range(2):
        dealer_hand.append(deck.pop(0))

    # Ukaze karty 
    print("Vaše karty:", player_hand)
    print("Karty dealera:", dealer_hand[:1], "[Otočená]")

    # Kontroluje jestli neni blackjack
    if "Eso" in player_hand and ("Jack" in player_hand or "Dama" in player_hand or "Kral" in player_hand):
        print("Blackjack!")

    # Hra
    while True:
        # Input od hrace

        print("Můžete vzít další kartu (h), nebo stát (s).")
        action = input("Co chcete udělat? ")

        # Hit
        if action == "h":
            # Bere dalsi kartu
            player_hand.append(deck.pop(0))
            print("Vaše karty:", player_hand)

            # Kontroluje jestli neni blackjack
            if "Eso" in player_hand and ("Jack" in player_hand or "Dama" in player_hand or "Kral" in player_hand):
                print("Blackjack!")
                break

            # Kontroluje jestli neni bust (pres 21)
            if sum([int(card.split()[0]) if card.split()[0].isdigit() else 10 for card in player_hand]) > 21:
                print_red("Přestřelil jsi!")
                break

        # Stay
        elif action == "s":
            break

        # Spatny input od hrace
        else:
            print("Zkuste to znovu.")

    # Dealerovo kolo
    print("Hraje dealer..")

    # Dealer bere kartu, pokud nema v ruce vic jak 17
    while sum([int(card.split()[0]) if card.split()[0].isdigit() else 10 for card in dealer_hand]) < 17:
        dealer_hand.append(deck.pop(0))
        print("Karty dealera:", dealer_hand)

    # Vypocet skore hrace a dealera
    player_score = sum([int(card.split()[0]) if card.split()[0].isdigit() else 10 for card in player_hand])
    dealer_score = sum([int(card.split()[0]) if card.split()[0].isdigit() else 10 for card in dealer_hand])

    # Tiskne vysledek a rozdava penize
    print("Vaše skóre:", player_score)
    print("Dealerovo skóre:", dealer_score)
    if player_score > 21:
        print_red("Prohrál jsi.")
    elif dealer_score > 21 or player_score > dealer_score:
        konto = konto - bet + bet*3
        print_green("Vyhrál jsi! Vyhráváš: "+ str(bet*3))
    elif player_score < dealer_score:
        print_red("Prohrál jsi.")
    else:
        konto = konto - bet + bet
        print("Remíze, získáváš zpět svou sázku: ",bet)

def kone():
    global konto
    while True:
        bet = int(input("Zadejte sázku prosím: "))
        if bet > konto:
            print_yellow("Nemáte dostatek financí.")
            continue
        if bet <= konto:
            break
    Konici=['Jack','Jhonny','Hope','Julka','Alfie','George','Murphy']
    print(Konici, "\n")    
    výběr = input("Vyberte koně: ")
    vyhernikun = random.choice(Konici)
    if výběr == vyhernikun:
        print_green("Výhral kůň" + vyhernikun)
        konto = konto - bet + bet * 6
        print_green("Výhra činí "+ str(bet*6))
    else:
        konto = konto - bet
        print_red("Prohra vyhrál kůň",vyhernikun)    

def automat():
    global bet_mat
    def automat_choice():
        global konto
        
        print("")
        print_magenta("Jaký automat chcete hrát?")
        print("")
        print_cyan("1. Mystery Play")
        print_pink("2. BAR Jackpot")
        print_cyan("3. Respin Hearts")
        print_pink("0. Odejít")
        print("")
        print_yellow("Váš aktuální zůstatek: "+ str(konto))
        
        choice = input("Vyberte operaci (1/2/3/0): ")
        if choice == "1":
            automat_mystery_set()
            automat_mystery()
        elif choice == '2':
            automat_bar_set()
            automat_bar()
        elif choice == '3':
            automat_respin_set()
            automat_respin()
        elif choice == '0':
            casino()
        else:
            print("Neplatná volba")
            automat_choice()
            
    def automat_mystery_set():
        global konto
        global bet_mat
        
        choice = input("Za kolik chcete točit? (5 / 10 / 20 / 50 / 100 / 200 / 500 / 1000): ")
        choice = int(choice)
        if choice > konto:
            print_yellow("Nemáte dostatek financí.")
            automat_choice()
        else:
            if choice == 5:
                bet_mat = 5
            elif choice == 10:
                bet_mat = 10
            elif choice == 20:
                bet_mat = 20
            elif choice == 50:
                bet_mat = 50
            elif choice == 100:
                bet_mat = 100
            elif choice == 200:
                bet_mat = 200
            elif choice == 500:
                bet_mat = 500
            elif choice == 1000:
                bet_mat = 1000
            else:
                print("Neplatná volba")
                automat_mystery_set()
        
        choice_spin = input("Chcete automatické otáčky? (A / N): ")
        if choice_spin == "A" or choice_spin == "a":
            spin = input("Kolikrát chcete točit? (5 / 10 / 15... ): ")
            spin = int(spin)
            if spin*bet_mat > konto:
                print_yellow("Nemáte dostatek financí.")
                automat_mystery_set()
            else:
                try:
                    for i in range(spin):
                        automat_mystery()
                    automat_mystery_end()
                except ValueError:
                    print("Neplatná volba")
                    automat_mystery_set()
        elif choice_spin == "N" or choice_spin == "n":
            automat_mystery()
            automat_mystery_end()
        else:
            print("Neplatná volba")
            automat_mystery_set()

    def automat_mystery():
        global konto
        global bet_mat
        
        wheel1 = random.choice(["�","6","?","X","♦"])
        wheel2 = random.choice(["�","6","?","X","♦"])
        wheel3 = random.choice(["�","6","?","X","♦"])
        wheel4 = random.choice(["�","6","?","X","♦"])
        wheel1_1 = random.choice(["�","6","?","X","♦"])
        wheel2_1 = random.choice(["�","6","?","X","♦"])
        wheel3_1 = random.choice(["�","6","?","X","♦"])
        wheel4_1 = random.choice(["�","6","?","X","♦"])
        wheel1_2 = random.choice(["�","6","?","X","♦"])
        wheel2_2 = random.choice(["�","6","?","X","♦"])
        wheel3_2 = random.choice(["�","6","?","X","♦"])
        wheel4_2 = random.choice(["�","6","?","X","♦"])
        print(wheel1,"-",wheel2,"-",wheel3,"-",wheel4)
        print(wheel1_1,"-",wheel2_1,"-",wheel3_1,"-",wheel4_1)
        print(wheel1_2,"-",wheel2_2,"-",wheel3_2,"-",wheel4_2)
        #Radky na � JACKPOT
        if wheel1 == wheel2 == wheel3 == wheel4 == "�" or wheel1_1 == wheel2_1 == wheel3_1 == wheel4_1 == "�" or wheel1_2 == wheel2_2 == wheel3_2 == wheel4_2 == "�":
            win = bet_mat*16
            konto = konto - bet_mat + bet_mat*16
            print_green("Vyhráváš MEGABONUS! Výhra x16: " + str(win))
        #Radky na ? JACKPOT
        elif wheel1 == wheel2 == wheel3 == wheel4 == "?" or wheel1_1 == wheel2_1 == wheel3_1 == wheel4_1 == "?" or wheel1_2 == wheel2_2 == wheel3_2 == wheel4_2 == "?":
            win = bet_mat*8
            konto = konto - bet_mat + bet_mat*8
            print_green("Vyhráváš BONUS! Výhra x8: " + str(win))
        #Radky na prvni tri mista
        elif wheel1 == wheel2 == wheel3 or wheel1_1 == wheel2_1 == wheel3_1 or wheel1_2 == wheel2_2 == wheel3_2:
            win = bet_mat*4
            konto = konto - bet_mat + bet_mat*4
            print_green("Vyhráváš BONUS! Výhra x4: " + str(win))
        #Diagonaly    
        elif wheel1 == wheel2_1 == wheel3_2 or wheel1_2 == wheel2_1 == wheel3:
            win = bet_mat*3
            konto = konto - bet_mat + bet_mat*3
            print_green("Vyhrál jsi! Výhra x3: " + str(win))
        #Prohra     
        else:
            konto = konto - bet_mat
            print_red("Prohrál jsi!")

    def automat_mystery_end():
        global konto
        global bet_mat
        
        answer = input("S = spin / R = nastaveni / E = konec: ")
        if answer == "S" or answer == "s" or answer == "spin":
            if bet_mat > konto:
                print_yellow("Nemáte dostatek financí.")
                automat_choice()
            else:
                automat_mystery()
                automat_mystery_end()
        elif answer == "R" or answer == "r" or answer == "nastaveni":
            automat_mystery_set()
        elif answer == "E" or answer == "e" or answer == "konec":
            automat_choice()
        else:
            print("Neplatná volba")
            automat_mystery_end()

    def automat_bar_set():
        global konto
        global bet_mat
        
        choice = input("Za kolik chcete točit? (5 / 10 / 20 / 50 / 100 / 200 / 500 / 1000): ")
        choice = int(choice)
        if choice > konto:
            print_yellow("Nemáte dostatek financí.")
            automat_choice()
        else:
            if choice == 5:
                bet_mat = 5
            elif choice == 10:
                bet_mat = 10
            elif choice == 20:
                bet_mat = 20
            elif choice == 50:
                bet_mat = 50
            elif choice == 100:
                bet_mat = 100
            elif choice == 200:
                bet_mat = 200
            elif choice == 500:
                bet_mat = 500
            elif choice == 1000:
                bet_mat = 1000
            else:
                print("Neplatná volba")
                automat_bar_set()
            
        choice_spin = input("Chcete automatické otáčky? (A / N): ")
        if choice_spin == "A" or choice_spin == "a":
            spin = input("Kolikrát chcete točit? (5 / 10 / 15... ): ")
            spin = int(spin)
            if spin*bet_mat > konto:
                print_yellow("Nemáte dostatek financí.")
                automat_bar_set()
            else:
                try:
                    for i in range(spin):
                        automat_bar()
                    automat_bar_end()
                except ValueError:
                    print("Neplatná volba")
                    automat_bar_set()
        elif choice_spin == "N" or choice_spin == "n":
            automat_bar()
            automat_bar_end()
        else:
            print("Neplatná volba")
            automat_bar_set()
            
    def automat_bar():
        global konto
        global bet_mat
        
        wheel1 = random.choice(["BAR"," 7 "," ! ","xXx"," ☺ "," ☻ "])
        wheel2 = random.choice(["BAR"," 7 "," ! ","xXx"," ☺ "," ☻ "])
        wheel3 = random.choice(["BAR"," 7 "," ! ","xXx"," ☺ "," ☻ "])
        wheel1_1 = random.choice(["BAR"," 7 "," ! ","xXx"," ☺ "," ☻ "])
        wheel2_1 = random.choice(["BAR"," 7 "," ! ","xXx"," ☺ "," ☻ "])
        wheel3_1 = random.choice(["BAR"," 7 "," ! ","xXx"," ☺ "," ☻ "])
        wheel1_2 = random.choice(["BAR"," 7 "," ! ","xXx"," ☺ "," ☻ "])
        wheel2_2 = random.choice(["BAR"," 7 "," ! ","xXx"," ☺ "," ☻ "])
        wheel3_2 = random.choice(["BAR"," 7 "," ! ","xXx"," ☺ "," ☻ "])
        print(wheel1,"-",wheel2,"-",wheel3)
        print(wheel1_1,"-",wheel2_1,"-",wheel3_1)
        print(wheel1_2,"-",wheel2_2,"-",wheel3_2)
        #Radky na BAR JACKPOT
        if wheel1 == wheel2 == wheel3 == "BAR" or wheel1_1 == wheel2_1 == wheel3_1 == "BAR" or wheel1_2 == wheel2_2 == wheel3_2 == "BAR":
            win = bet_mat*15
            konto = konto - bet_mat + bet_mat*15
            print_green("Vyhráváš MEGABONUS! Výhra x15: " + str(win))
        # Radky na  7 
        elif wheel1 == wheel2 == wheel3 == " 7 " or wheel1_1 == wheel2_1 == wheel3_1 == " 7 " or wheel1_2 == wheel2_2 == wheel3_2 == " 7 ":
            win = bet_mat*15
            konto = konto - bet_mat + bet_mat*10
            print_green("Vyhráváš BONUS! Výhra x10: " + str(win))
        # Radky na !
        elif wheel1 == wheel2 == wheel3 == " ! " or wheel1_1 == wheel2_1 == wheel3_1 == " ! " or wheel1_2 == wheel2_2 == wheel3_2 == " ! ":
            win = bet_mat*5
            konto = konto - bet_mat + bet_mat*5
            print_green("Vyhráváš BONUS! Výhra x5: " + str(win))
        # Radky    
        elif wheel1 == wheel2 == wheel3 or wheel1_1 == wheel2_1 == wheel3_1 or wheel1_2 == wheel2_2 == wheel3_2:
            win = bet_mat*3
            konto = konto - bet_mat + bet_mat*3
            print_green("Vyhrál jsi! Výhra x3: " + str(win))
        #Diagonaly    
        elif wheel1 == wheel2_1 == wheel3_2 or wheel1_2 == wheel2_1 == wheel3:
            win = bet_mat*2
            konto = konto - bet_mat + bet_mat*2
            print_green("Vyhrál jsi! Výhra x2: " + str(win))
        #Zbytek - prvni dva valce
        elif wheel1 == wheel2 or wheel1_1 == wheel2_1 or wheel1_2 == wheel2_2:    
            win = bet_mat*1
            konto = konto - bet_mat + bet_mat*1
            print_green("Vyhrál jsi! Výhra x1: " + str(win))   
        #Prohra     
        else:
            konto = konto - bet_mat
            print_red("Prohrál jsi!")

    def automat_bar_end():
        global konto
        global bet_mat
        
        answer = input("S = spin / R = nastaveni / E = konec: ")
        if answer == "S" or answer == "s" or answer == "spin":
            if bet_mat > konto:
                print_yellow("Nemáte dostatek financí.")
                automat_choice()
            else: 
                automat_bar()
                automat_bar_end()
        elif answer == "R" or answer == "r" or answer == "nastaveni":
            automat_bar_set()
        elif answer == "E" or answer == "e" or answer == "konec":
            automat_choice()
        else:
            print("Neplatná volba")
            automat_bar_end()

    def automat_respin_set():
        global konto
        global bet_mat
        
        choice = input("Za kolik chcete točit? (5 / 10 / 20 / 50 / 100 / 200 / 500 / 1000): ")
        choice = int(choice)
        if choice > konto:
            print_yellow("Nemáte dostatek financí.")
            automat_choice()
        else:
            if choice == 5:
                bet_mat = 5
            elif choice == 10:
                bet_mat = 10
            elif choice == 20:
                bet_mat = 20
            elif choice == 50:
                bet_mat = 50
            elif choice == 100:
                bet_mat = 100
            elif choice == 200:
                bet_mat = 200
            elif choice == 500:
                bet_mat = 500
            elif choice == 1000:
                bet_mat = 1000
            else:
                print("Neplatná volba")
                automat_respin_set()
        
        choice_spin = input("Chcete automatické otáčky? (A / N): ")
        if choice_spin == "A" or choice_spin == "a":
            spin = input("Kolikrát chcete točit? (5 / 10 / 15... ): ")
            spin = int(spin)
            if spin*bet_mat > konto:
                print_yellow("Nemáte dostatek financí.")
                automat_respin_set()
            else:
                try:
                    spin = int(spin)
                    for i in range(spin):
                        automat_respin()
                    automat_respin_end()
                except ValueError:
                    print("Neplatná volba")
                    automat_respin_set()
        elif choice_spin == "N" or choice_spin == "n":
            automat_respin()
            automat_respin_end()
        else:
            print("Neplatná volba")
            automat_respin_set()

    def automat_respin():
        global konto
        global bet_mat
        
        wheel1 = random.choice(["SPIN","SPIN","SPIN"," ♣♣ "," !! ","xXXx"," ☺☻ "," ☺☻ "])
        wheel2 = random.choice(["SPIN","SPIN","SPIN"," ♣♣ "," !! ","xXXx"," ☺☻ "," ☺☻ "])
        wheel3 = random.choice(["SPIN","SPIN","SPIN"," ♣♣ "," !! ","xXXx"," ☺☻ "," ☺☻ "])
        wheel1_1 = random.choice(["SPIN","SPIN","SPIN"," ♣♣ "," !! ","xXXx"," ☺☻ "," ☺☻ "])
        wheel2_1 = random.choice(["SPIN","SPIN","SPIN"," ♣♣ "," !! ","xXXx"," ☺☻ "," ☺☻ "])
        wheel3_1 = random.choice(["SPIN","SPIN","SPIN"," ♣♣ "," !! ","xXXx"," ☺☻ "," ☺☻ "])
        wheel1_2 = random.choice(["SPIN","SPIN","SPIN"," ♣♣ "," !! ","xXXx"," ☺☻ "," ☺☻ "])
        wheel2_2 = random.choice(["SPIN","SPIN","SPIN"," ♣♣ "," !! ","xXXx"," ☺☻ "," ☺☻ "])
        wheel3_2 = random.choice(["SPIN","SPIN","SPIN"," ♣♣ "," !! ","xXXx"," ☺☻ "," ☺☻ "])

        print(wheel1,"-",wheel2,"-",wheel3)
        print(wheel1_1,"-",wheel2_1,"-",wheel3_1)
        print(wheel1_2,"-",wheel2_2,"-",wheel3_2)

        # Zatočení zdarma pokud padnout tři SPIN
        if wheel1 == wheel2 == wheel3 == "SPIN" or wheel1_1 == wheel2_1 == wheel3_1 == "SPIN" or wheel1_2 == wheel2_2 == wheel3_2 == "SPIN":
            print("RESPIN! Točíš znovu zadarmo!")
            automat_respin()
        # Radky na ♣♣ 
        elif wheel1 == wheel2 == wheel3 == " ♣♣ " or wheel1_1 == wheel2_1 == wheel3_1 == " ♣♣ " or wheel1_2 == wheel2_2 == wheel3_2 == " ♣♣ ":
            win = bet_mat*5
            konto = konto - bet_mat + bet_mat*5
            print_green("Vyhráváš BONUS! Výhra x5: " + str(win))
        #Diagonaly    
        elif wheel1 == wheel2_1 == wheel3_2 or wheel1_2 == wheel2_1 == wheel3:
            win = bet_mat*2
            konto = konto - bet_mat + bet_mat*2
            print_green("Vyhrál jsi! Výhra x2: " + str(win))
        # Radky
        elif wheel1 == wheel2 == wheel3 or wheel1_1 == wheel2_1 == wheel3_1 or wheel1_2 == wheel2_2 == wheel3_2:
            win = bet_mat*3
            konto = konto - bet_mat + bet_mat*3
            print_green("Vyhrál jsi! Výhra x3: " + str(win))
        #Zbytek - prvni dva valce
        elif wheel1 == wheel2 or wheel1_1 == wheel2_1 or wheel1_2 == wheel2_2:    
            win = bet_mat*1
            konto = konto - bet_mat + bet_mat*1
            print_green("Vyhrál jsi! Výhra x1: " + str(win))   
        #Prohra     
        else:
            konto = konto - bet_mat
            print_red("Prohrál jsi!")
            
    def automat_respin_end():
        global konto
        global bet_mat
        answer = input("S = spin / R = nastaveni / E = konec: ")
        if answer == "S" or answer == "s" or answer == "spin":
            if bet_mat > konto:
                print_yellow("Nemáte dostatek financí.")
                automat_choice()
            else:
                automat_respin()
                automat_respin_end()
        elif answer == "R" or answer == "r" or answer == "nastaveni":
            automat_respin_set()
        elif answer == "E" or answer == "e" or answer == "konec":
            automat_choice()
        else:
            print("Neplatná volba")
            automat_respin_end()

    automat_choice()

def coinflip():
    global konto
    bet = konto
    win = random.randint(0, 1)
    print("Panna nebo Orel?")
    print("Pro pannu zadejte 1, pro orel zadejte 2")
    choice = input("1 or 2: ")
    
    if choice in ('1', '2'):
        if (choice == "1" and win == 0) or (choice == "2" and win == 1):
            print_green("Vyhrál jste")
            konto += bet * 100
        else:
            print_red("Prohrál jste")
            konto = konto - bet
    else:
        print("Neplatná volba")

def bingo():
    global konto
    while True:
        bet = int(input("Zadejte sázku prosím: "))
        if bet > konto:
            print_yellow("Nemáte dostatek financí.")
            continue
        if bet <= konto:
            break

    w = random.randint(8,20)       
    def generate_bingo_card():
        card = []
        for i in range(5):
            column = random.sample(range(1 + i * 15, 16 + i * 15), 5)
            card.extend(column)
        card[12] = "X"
        return card

    def display_bingo_card(card):
        print(" B   I   N   G   O")
        for i in range(5):
            for j in range(5):
                if i == 2 and j == 2:
                    print("|  " + str(card[i * 5 + j]) + " ", end="")
                else:
                    print("| " + str(card[i * 5 + j]) + " ", end="")
            print("|")

    def check_bingo(card, drawn_numbers):
        rows = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
        cols = [[0, 5, 10, 15, 20], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24]]
        diagonals = [[0, 6, 12, 18, 24], [4, 8, 12, 16, 20]]

        for row in rows:
            if all(number in drawn_numbers for number in [card[i] for i in row]):
                return True

        for col in cols:
            if all(number in drawn_numbers for number in [card[i] for i in col]):
                return True

        for diagonal in diagonals:
            if all(number in drawn_numbers for number in [card[i] for i in diagonal]):
                return True

        return False

    def play_bingo():
        print("Bingo Imperial")
        input("Stiskni ENTER pro pokračovaní...")
        card = generate_bingo_card()
        display_bingo_card(card)

        drawn_numbers = set()
    for turn in range(1, 21):
        w = random.randint(5,10)
        input("Stiskni ENTER pro pokračovaní...")
        drawn_number = random.randint(1, 75)
        print("Tažené č:", drawn_number)
        drawn_number.add(drawn_number)
        if drawn_number in card:
            card[card.index(drawn_number)] = "X"
        display_bingo_card(card)
        if check_bingo(card, drawn_number):
            konto = konto + bet*1.5
            print("Bingo! Vyhrál jste",konto)
            break
        if turn == w:
            print("Prohra.")
            konto = konto - bet

    play_bingo()

        


def casino():
    print_magenta("KASINO IMPERIAL (PYTHON)")
    
    print_magenta("Kam chcete jít?")
    print_pink("1. Pokladna")
    print_cyan("2. Ruleta")
    print_pink("3. Blackjack")
    print_cyan("4. Sazeni na koně")
    print_pink("5. Automaty")
    print_cyan("6. Bingo")
    print_pink("7. Coinflip")
    print_cyan("0. Odejít")

    choice = input("Vyberte operaci (0/1/2/3/4/5/6/7): ")
    if choice in ('1', '2', '3', '4', '5', '6', '7', "0"):
        if choice == '1':
            penize()
        if choice == '2':
            while True:
                rulleta()
                answer = input("Chcete pokračovat? (ano/ne): ")
                if answer.lower() != 'ano':
                    casino()
        elif choice == '3':
            while True:
                Blackjack()
                answer = input("Chcete pokračovat? (ano/ne): ")
                if answer.lower() != 'ano':
                    casino()
        elif choice == '4':
            while True:
                kone()
                answer = input("Chcete pokračovat? (ano/ne): ")
                if answer.lower() != 'ano':
                    casino()
        elif choice == '5':
            automat()
        elif choice == '6':
            while True:
                bingo()
                answer = input("Chcete pokračovat? (ano/ne): ")
                if answer.lower() != 'ano':
                    casino()
        elif choice == '7':
            while True:
                coinflip()
                answer = input("Chcete pokračovat? (ano/ne): ")
                if answer.lower() != 'ano':
                    casino()
        elif choice == '0':a
            quit()
        else:
            print("Neznámá operace.")


casino()
