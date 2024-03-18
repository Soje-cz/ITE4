import random
import msvcrt

print("Vítejte v Casinu imperial")

def konto():
    global konto
    konto = int(input("Vložte finanční prostředky: "))
    casino()

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
            print("Došli vám peníze.")
            return False
        return True

def Blackjack():
    pack 

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
        print("prohra vyhrál kůň",vyhernikun)    
        
    


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
            konto()
        if choice == '2':
            while True:
                rulleta()
                answer = input("Chcete pokračovat? (ano/ne): ")
                if answer.lower() != 'ano':
                    casino()
        elif choice == '3':
            print("Tato sekce zatím není otevřena")
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
