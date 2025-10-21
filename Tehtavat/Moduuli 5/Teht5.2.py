
#Tehdään lista, johon luvut tallentuu
luvut = []

#while silmukka, joka toistaa itsensä niin monta kertaa kunnes syötetään tyhjä arvo.
while True:
    arvot = input("Syötä luku tai tyhjä arvo: ")
    if arvot == "":
        break
    try:
        luku = float(arvot)
        luvut.append(luku)
    except ValueError:
        print("Arvon oltava luku")

#Käännetään luvut suuruus järjejestykseen
luvut.sort(reverse=True)


#Printataan suurimmat viisi lukua.
print("Suurimmat viisi: ")

for i in range(min(5, len(luvut))):
    print(luvut[i])




