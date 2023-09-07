import random as rd
import numpy as np


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

def anvendelse_løkker():
    total = 0
    i = 0

    while i <= 100:
        total = total + i
        i = i + 1
    print(total)

def anvendelse_løkker2():
    total = 0
    tall = int(input("Vennligst skriv inn et tall: "))

    for i in range(tall):
        total = total + i
    
    print(total)

def nøstet_løkke():
    for i in range(1, 6):
        for j in range(1, 11):
            print(f"{(i * j):4}", end=" ")
        print("")

def gjennomsnitt_sum():
    n = int(input("Vennligst skriv inn en tall: "))
    total = 0

    for i in range (1, n+1):
        total = total + i
    gjennomsnitt = total / n

    print(f"Summen av tallene fra 1 til og med {n} er {total}.")
    print(f"Gjennomsnittet er {gjennomsnitt}")


def liste1():
    verdensdeler = ["Afrika", "Asia", "Europa", "Nord-Amerika", "Sør-Amerika", "Oceania", "Antarktika"]
    heltall = list(range(1, 51))
    oddetall = list(range(1, 101, 2))

    print(verdensdeler[0])
    print(verdensdeler[4])
    print(verdensdeler[-1])
    print(heltall)
    print(oddetall)

def liste2():
    liste = list(range(1, 21))  
    partall = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    print("Opprinnelig liste:", liste)

    for i in partall:
        if i in liste:
            liste.remove(i)  # Fjern partall som finnes i partall-listen fra liste

    print("Endret liste:", liste)

def liste3():
    liste = [1, 6, 3, 4, 2, 3, 5, 7, 8, 3, 3, 3, 2, 3, 4, 6, 7, 3, 4, 3, 3]

    for i in liste:
        if 3 in liste:
            liste.remove(3)
    
    print(liste)

def array():
    tall = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(tall * 2)

array()
