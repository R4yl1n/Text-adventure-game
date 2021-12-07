import time
import random

someThing = "press something to continue"

game_goes_on = True
hearts = 10

class Person():

    def checkIfAlive(self):
        if hearts == 0:
            print("Du bist gestorben das spiel wird beendet!")
            input_ok = False
        else:
            print(f"du hast noch {hearts} Lebenspunkte")
            #continue

player = Person()
playerName = input("Wie ist dein Name spieler? ")    

print(f"Wir haben das Jahr 1562 dein Name ist {playerName} du bestreitest das letze Lvl und tritts jetzt gegen den endgegner an.")
time.sleep(2)
print("auf einmal hörrst du schwere schritte die den Boden beben lassen .")


input(someThing)

Bernhard = Person()
print(f"Bernhard greifft dich an!")
time.sleep(2)

bhLife = 10
while bhLife > 0 and hearts > 0:                #first fight Bernhard = bhLife
    
    n = random.randint(1,100)
    if n < 30:
        print("Bernhard hat dich getackelt du verlierst 2 Schadenspunkt")
        hearts -= 2
        input(someThing)
        player.checkIfAlive()

    elif n < 60 and n > 30:
        print("Bernhard hat sein schwert gezogen und schlägt dich damit, du verlierst 3 Schadenspunkte")
        hearts -= 3
        input(someThing)
        player.checkIfAlive()

    elif n < 85 and n > 60:
        print(" Bernhard hat sein schwert gezogen und schlägt dich damit, jedoch konntest du ausweichen und verlierst keine Lebenspunkte!")
        input(someThing)
        player.checkIfAlive()

    else:
        print(" Bernhard hollt ein Brennender pfeilbogen raus der dich in Flammen steckt, du verlierst 4 Schadenspunkte")
        hearts -= 4
        input(someThing)
        player.checkIfAlive()

    

    input_ok = True
    while input_ok == True:
        if hearts <= 0:
            break
        
        attack = input("Wie willst du angreifen 1. Schwerthieb (2Hp) , 2. pfeil schiessen (1Hp), 3. Heilung (+3Hp) ") #first ight
        if attack == "1":
            print("Du greiffst an in dem du ihn mit einem schwert hieb angreiffst")
            input("press any button")
            print("Dies verursacht 2 schadenpunkte")
            bhLife -= 2
            time.sleep(1)
            print(f"Bernhard hat noch {bhLife} Lebenspunkte")
            input(someThing) 
            input_ok = False

        elif attack == "2":
            print("Du greiffst an in dem du ihn mit einen pfeil schiesst mit deinem Bogen")
            print("pres any button")
            print("Dies verursacht 1 Schadenspunkt")
            bhLife -= 1
            time.sleep(1)
            print(f"Bernhard hat noch {bhLife} Lebenspunkte")
            input(someThing)
            input_ok = False
        
        elif attack == "3":
            print("Du heillst dich selber und erhälst 3 Lebenspunkte")
            hearts += 3
            if hearts > 9:
                hearts -= 2
                print("du hast schon die Maximale Lebenspunkte erreicht")
                print("bitte wähle eine andere Attacke")
                input(someThing)
            else:
                input_ok = False
                input(someThing)

if player.checkIfAlive() == True:
    print("Der kampf ist beendet du hast gewonnen")
    input(someThing)
