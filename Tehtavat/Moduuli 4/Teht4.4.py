#Peli, jossa tietokone arpoo kokonaisluvun väliltä 1-10

#Arvotaan ensiksi luku 1-10 väliltä
import random

luku = int(random.randint(1,10))

#Pyydetään käyttäjältä kokonaisluku
arvaus = int(input("Arvaa kokonaisluku 1-10 välillä: "))

#vertaillaan arvoja, printataan käyttäjälle vastaus ja vertaillaan arvoja
while luku is not arvaus:
    if arvaus < luku:
        print("Liian pieni arvaus")
    if arvaus > luku:
        print("Liian suuri arvaus")
    if arvaus is not luku:
        arvaus = int(input("Arvaa uudelleen: "))

#Jos arvaus oikein printataan oikein-
print("Oikein")

