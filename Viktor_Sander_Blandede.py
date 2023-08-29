# OPPGAVE 1:
# I Kode 1 vil kjøre begge if-statementene bli kjørt og X og Y variablene blir begge sjekket og
# Antallpositive vil bli større om variablene har en verdi over 0.
# I Kode 2 sjekker vi også verdien til variablene X & Y, men her kjøres bare en av if-statementsene.
# Kode 2 sjekker først om x er større enn 0, dermed plusser den opp antallpositive, om dette ikke er TRUE
# sjekker den dermed Y. Så forskjellen mellom disse kodene er rett og slett antall if-statements som blir sjekket

def karaktersjekker():
    score = int(input("Skriv inn din poengscore: "))

    if score < 0 or score > 100:
        print("Ugyldig poengscore!")
    else:
        if score <= 20:
            print("Du har fått karakter 1!")
        elif score <= 40:
            print("Du har fått karakter 2!")
        elif score <= 60:
            print("Du har fått karakter 3!")
        elif score <= 80:
            print("Du har fått karakter 4!")
        elif score <= 90:
            print("Du har fått karakter 5!")
        elif score <= 100:
            print("Du har fått karakter 6!")

# OPPGAVE 3
# I oppgaven/koden ovenfor kan du se et eksempel på at rekkefølge har betydning.
# Hvis vi for eksempel bytter karakterscore 5 og 6, er ikke 6 lenger oppnåelig.
# I koden ovenfor sjekker programmet kontinuerlig poengscoren til brukeren for å så dele ut en karakter,
# Om statementen blir false, går den da ned et hakk og sjekker dermed igjen om brukeren har mottatt den karakteren.
# Bytter man rekekfølge på tallene blir dette feil.
#-------------------------------------------------------
# På Oppgave 5 kan man se et eksempel hvor if statementene ikke har mye betydning på rekkefølge.
# Om vi bytter om elif statementen til for eksempel if, så sjekker den begge uansett og dermed har det veldig lite å si
# hvem som kommer først siden både Celcius og Fahrenheit overlapper ikke hverandre. 


    
def oppgave4():
    tall1 = int(input("Skriv inn tall 1: "))
    tall2 = int(input("Skriv inn tall 2: "))
    tall3 = int(input("Skriv inn tall 3: "))

    if tall1 == tall2 == tall3:
        print("Alle tallene har lik verdi.")
    else:
        print("Tallene har ikke lik verdi.")

def oppgave4b():
    tall1 = int(input("Vennligst skriv inn et tall: "))
    tall1 = int(tall1 % 2)

    if tall1 == 0:
        print("Tallet du oppga er et partall!")
    else:
        print("Tallet du oppga var et oddetall")

def oppgave4c():
    tall1 = int(input("Vennligst skriv inn det første tallet: "))
    tall2 = int(input("Vennligst skriv inn det andre tallet: "))
    tall3 = int(input("Vennligst skriv inn det tredje tallet: "))

    størst = tall1

    if tall2 > størst:
        størst = tall2
    if tall3 > størst:
        størst = tall3
    
    print(str(størst) + " Var det største tallet du oppgave")

def oppgave5():
    temperatur = float(input("Hvilken temperatur ønsker du å omgjøre?: "))
    målingsenhet = str(input("Er temperaturen i målenheten C eller F?: "))

    if målingsenhet.upper() == "C":
        temperatur = temperatur * 1.8 + 32
        print("Temperaturen er", temperatur, "I Farenheit.")
    elif målingsenhet.upper() == "F":
        temperatur = (temperatur - 32) / 1.8
        print("Temperaturen er", temperatur, "I Celsius.")
    else:
        print("Ugyldig måleenhet")

karaktersjekker()