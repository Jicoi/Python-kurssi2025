

#Haetaan satunnaisten lukujen arpominen käyttöön.
import random

#kysytään käyttäjältä arvottavien noppien määrä.
nopat = int(input("Monta noppaa heität?: "))


#alustetaan noppien laskenta alkamaan nollasta
maara = 0


#Tehdään for silmukka, joka toistaa itsensä noppien lukumäärän verran. Asetetaan myös nopalle arvot 1-6
for i in range(nopat):
    heitto = random.randint(1, 6)
    print(f"Noppa {i + 1}: {heitto}")
    maara += heitto


#Lopuksi tulostetaan noppien summa
print(f"Noppien summa on: {maara}")


