import random
import msvcrt

print("Vítejte v Casinu imperial")

global konto

konto = 0

def penize():
    global konto
    if konto >= 0:
        print("Na vašem kontě je", konto)
        choice = input("Chcete vložit finanční prostředky? (ano/ne): ")
        if choice == "ano":
            add_konto = int(input("Zadejte čásku: "))
            konto = konto + add_konto
            print("Na vašem kontě máte ",konto, " korun.")
            casino()
        elif choice == "ne":
            casino()
        else:
            print("Toto nebyla možnost.")
            penize()

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

    print("Na co chcete vsadit:")
    print("1. Červená")
    print("2. Černá")
    print("3. Sudá")
    print("4. Lichá")
    print("5. Číslo")

    choice = input("Vyberte operaci (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        roll = random.randint(0, 36)
        if choice == '1':
            if roll in Red:
                konto = konto - bet + bet * 2
                print("Výhra!")
            else:
                konto -= bet
                print("Prohra.")
        elif choice == '2':
            if roll in Black:
                konto = konto - bet + bet * 2
                print("Výhra!")
            else:
                konto -= bet
                print("Prohra.")
        elif choice == '3':
            if roll in Even:
                konto = konto - bet + bet * 2
                print("Výhra!")
            else:
                konto -= bet
                print("Prohra.")
        elif choice == '4':
            if roll in Odd:
                konto = konto - bet + bet * 2
                print("Výhra!")
            else:
                konto -= bet
                print("Prohra.")
        elif choice == '5':
            cislo = int(input("Zadejte číslo na které chcete vsadit: "))
            if roll == cislo:
                konto = konto - bet + bet * 5
                print("Výhra!")
            else:
                konto -= bet
                print("Prohra.")

        print("Padlo číslo:", roll)
        print("Stav konta:", konto)

        if konto == 0:
            print("Došly vám peníze.")
            return False
        return True

def Blackjack():
    global konto
    while True:
        bet = int(input("Zadejte sázku prosím: "))
        if bet > konto:
            print("Nemáte dostatek financí.")
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
                print("Přestřelil jsi!")
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
        print("Prohrál jsi.")
    elif dealer_score > 21 or player_score > dealer_score:
        konto = konto - bet + bet*3
        print("Vyhrál jsi! Vyhráváš: ",bet*3)
    elif player_score < dealer_score:
        print("Prohrál jsi.")
    else:
        konto = konto - bet + bet
        print("Remíze, získáváš zpět svou sázku: ",bet)


def kone():
    global konto
    while True:
        bet = int(input("Zadejte sázku prosím: "))
        if bet > konto:
            print("Nemáte dostatek financí.")
            continue
        if bet <= konto:
            break
    Konici=['Jack','Jhonny','Hope','Julka','Alfie','George','Murphy']
    print(Konici, "\n")    
    výběr = input("Vyberte koně: ")
    vyhernikun = random.choice(Konici)
    if výběr == vyhernikun:
        print ("Výhral kůň", vyhernikun)
        konto = konto - bet + bet * 6
        print ("Vyhra činí", bet*6)
    else:
        konto = konto - bet
        print("Prohra vyhrál kůň",vyhernikun)    
        
    


def casino():
    print("Kam chcete jít")
    print("1. Pokladna")
    print("2. Ruleta")
    print("3. Blackjack")
    print("4. Sazeni na koně")
    print("5. Automaty")
    print("6. Bingo")

    choice = input("Vyberte operaci (1/2/3/4/5/6): ")
    if choice in ('1', '2', '3', '4', '5'):
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
            print("Tato sekce zatím není otevřena")
        elif choice == '6':
            print("Tato sekce zatím není otevřena")
        else:
            print("Neznámá operace.")


casino()
