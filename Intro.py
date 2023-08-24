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

partall()