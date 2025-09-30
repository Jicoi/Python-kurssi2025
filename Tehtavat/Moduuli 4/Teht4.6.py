#Tehdään algoritmi joka laskee piin likiarvon.

import random

#Ensiksi kysymme käyttäjältä pisteet
arvotut = int(input("Anna pisteet: "))

#Asetaan alkupisteet
n = 0
laskuri = 0

#Asetetaan arvot x ja y. Tarkastetaan mahtuuko ympyrä neliö sisälle.
while laskuri < arvotut:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
    laskuri += 1

#Lasketaan pii
likiarvo = 4 * n / arvotut

#Tulostetaan lopuksi tulokset
print("Piin likiarvo", likiarvo)

