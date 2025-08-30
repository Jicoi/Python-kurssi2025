#Tehtävä 4.1
#Ohjelma, joka käyttää while rakennetta.

#Asetaan arvon alin lukumäärä
arvo = 0

#Tehdään toistorakenne joka toistaa luvut 0-1000 välillä ja tulostaa 3:lla jaolliset luvut
while arvo <= 1000:
        arvo = arvo + 1
        if arvo % 3 == 0:
            print(arvo)
