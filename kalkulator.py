def kalkulator():
    print("[1] Pluss")
    print("[2] Minus")
    print("[3] Gange")
    print("[4] Dele")
    valg = int(input("Vennligst velg en regneprosess ved å skrive inn et nummer her: "))



    if valg > 4 or valg < 1:
        print("Du har ikke valgt en gyldig regneprosess")
    else:
        if valg == 1:
            x = int(input("Vennligst skriv inn første tall: "))
            y = int(input("Vennligst skriv inn siste tall: "))
            sum = x + y

            print(f"{x} + {y}", "=", sum)
        if valg == 2:
            x = int(input("Vennligst skriv inn første tall: "))
            y = int(input("Vennligst skriv inn siste tall: "))
            sum = x - y

            print(f"{x} - {y}", "=", sum)
        if valg == 3:
            x = int(input("Vennligst skriv inn første tall: "))
            y = int(input("Vennligst skriv inn siste tall: "))
            sum = x * y

            print(f"{x} * {y}", "=", sum)
        if valg == 4:
            x = int(input("Vennligst skriv inn første tall: "))
            y = int(input("Vennligst skriv inn siste tall: "))
            sum = x / y

            print(f"{x} / {y}", "=", sum)

kalkulator()
    
    