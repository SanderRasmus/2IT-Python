import random as rd

def hei():
    navn = str(input('Hva heter du? '))
    print('Hei ' + navn)


def kuprat():
    melding = str(input('Hva skal kua si? '))
    boblelengde = len(melding) + 2

    print(' ' + '_' * boblelengde)
    print('<' + melding + '>')
    print(' ' + '-' * boblelengde)
    print('     \   ^__^')
    print('      \  (oo)\_______')
    print('         (__)\       )')
    print('             ||----W |')
    print('             ||     ||')



### Oppgave 1 - Betingelser og Valg

def størsttall():
    a = int(input("Skriv inn Tall nummer 1! "))
    størst = a

    b = int(input("Skriv inn Tall nummer 2! "))
    
    if b > størst:
        størst = b

    c = int(input("Skriv inn Tall nummer 3! "))

    if c > størst:
        størst = c

    d = int(input("Skriv inn Tall nummer 4! "))

    if d > størst:
        størst = d

    e = int(input("Skriv inn Tall nummer 5! "))

    if e > størst:
        størst = e

    print("Det største tallet du oppga var: " + str(størst))


def partall():
    tall = int(input("Skriv inn et tall: "))
    tall = (tall % 2)

    if tall == 1:
        print("Dette tallet er et oddetall")
    else:
        print("Dette tallet er et partall")


def karaktersjekker():
    poengscore = int(input("Skriv inn din poengscore: "))

    if poengscore > 100 or poengscore < 0:
        print("Ugyldig poengscore")
    else: 
        if poengscore <= 20:
            print("Du har fått karakter 1!")
        elif poengscore <= 40:
            print("Du har fått karakter 2!")
        elif poengscore <= 60:
            print("Du har fått karakter 3!")
        elif poengscore <= 80:
            print("Du har fått karakter 4!")
        elif poengscore <= 90:
            print("Du har fått karakter 5!")
        elif poengscore <= 100:
            print("Du har fått karakter 6!")


def temperatur_konvertor():
    temperatur = float(input("Hvilken temperatur ønsker du å omgjøre?: "))
    målingsenhet = str(input("Er temperaturen i målenheten C eller F?: "))

    if målingsenhet.upper() == "C":
        temperatur = temperatur * 1.8 + 32
        print("Temperaturen er", temperatur, "I Farenheit")
    elif målingsenhet.upper() == "F":
        temperatur = (temperatur - 32) / 1.8
        print("Temperaturen er", temperatur, "I Celsius")
    else:
        print("Ugyldig måleenhet")


def løkke1():
    tekst_bruker = str(input("Skriv inn en tekst!: "))

    for i in tekst_bruker:
        print(i, end="#")
    
def løkke2():
    for i in range(1,51):
        print("Denne løkka har gjentatt seg " + str(i) + " antall ganger.")

def kvadrattall():
    makstall = 100
    i = 1

    while i**2 <= makstall:
        print(i**2)
        i +=1
    
def terning():
    totalsum = 0

    while totalsum != 7:
        terning1 = rd.randint(1, 6)
        terning2 = rd.randint(1, 6)

        totalsum = terning1 + terning2
        print("Terningene viser " + str(terning1) + " og " + str(terning2) +". Summen av terningene er: " + str(totalsum))

terning()