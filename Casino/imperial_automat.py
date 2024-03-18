import random

def automat():
    wheel1 = random.choice(["BAR","7","!","X","☺","☻"])
    wheel2 = random.choice(["BAR","7","!","X","☺","☻"])
    wheel3 = random.choice(["BAR","7","!","X","☺","☻"])
    wheel1_1 = random.choice(["BAR","7","!","X","☺","☻"])
    wheel2_1 = random.choice(["BAR","7","!","X","☺","☻"])
    wheel3_1 = random.choice(["BAR","7","!","X","☺","☻"])
    wheel1_2 = random.choice(["BAR","7","!","X","☺","☻"])
    wheel2_2 = random.choice(["BAR","7","!","X","☺","☻"])
    wheel3_2 = random.choice(["BAR","7","!","X","☺","☻"])
    print(wheel1,"-",wheel2,"-",wheel3)
    print(wheel1_1,"-",wheel2_1,"-",wheel3_1)
    print(wheel1_2,"-",wheel2_2,"-",wheel3_2)
    #Radky na BAR
    if wheel1 == wheel2 == wheel3 == "BAR" or wheel1_1 == wheel2_1 == wheel3_1 == "BAR" or wheel1_2 == wheel2_2 == wheel3_2 == "BAR":
        print("Vyhráváš MEGABONUS! Výhra x15:")
    # Radky na 7    
    elif wheel1 == wheel2 == wheel3 == "7" or wheel1_1 == wheel2_1 == wheel3_1 == "7" or wheel1_2 == wheel2_2 == wheel3_2 == "7":
        print("Vyhráváš BONUS! Výhra x10: ")
    # Radky na !    
    elif wheel1 == wheel2 == wheel3 == "!" or wheel1_1 == wheel2_1 == wheel3_1 == "!" or wheel1_2 == wheel2_2 == wheel3_2 == "!":
        print("Vyhráváš BONUS! Výhra x5: ")
    # Radky    
    elif wheel1 == wheel2 == wheel3 or wheel1_1 == wheel2_1 == wheel3_1 or wheel1_2 == wheel2_2 == wheel3_2:
        print("Vyhrál jsi! Výhra x3:")
    #Diagonaly    
    elif wheel1 == wheel2_1 == wheel3_2 or wheel1_2 == wheel2_1 == wheel3:
        print("Vyhrál jsi! Výhra x2: ")
    #Zbytek - prvni dva valce
    elif wheel1 == wheel2 or wheel1_1 == wheel2_1 or wheel1_2 == wheel2_2:    
        print("Vyhrál jsi! Výhra x1: ")   
    #Prohra     
    else:
        print("Prohrál jsi!")    
