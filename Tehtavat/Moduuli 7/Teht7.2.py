#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon.

#tehdään tyhjä joukko, johon käyttäjän syöttämät nimet laitetaan
nimet = set()

#silmukka, joka lisää nimet joukkoon tai lopettaa kyselyn tyhjällä arvolla.
while True:
    nimi = input("Syötä nimi tai tyhjä: ") #kysyy käyttäjää syöttämään nimen tai päättämään loopin
    if nimi in nimet:
        print("Aiemmin syötetty nimi") #tarkastaa onko nimi duplikkaatti
    else:
        print("Uusi nimi") # ilmoittaa onko nimi uusi arvo
        nimet.add(nimi)  #lisää nimen joukkoon
    if nimi  == "":break # katkaisee loopin


print("Syötetyt nimet: ")
for x in nimet: # tulostaa syötetyt nimet
    print(x)