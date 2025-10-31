# Parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun 1-6
# joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.


# Ensiksi tuodaan random kirjasto
import random


# Tehdään funktio, joka tuo nopan arvon väliltä 1-6
def noppa():
    return random.randint(1, 6)             # return = lopettaa funktion ja palauttaa arvon


# funktio, joka jatkuu niin pitkään kunnes tulee kutonen.
def kutonen(noppa):
    print(f"Heitto: {noppa}")       # tulostaa arvotun heiton.
    if noppa == 6:                  # if noppa vertaa funktion arpomia arvoja ja lopettaa sen jos arvo on 6
        exit()


# while true looppi jatkuu niin pitkään kunnes saadaan arvo kuusi.
while True:
    kutonen(noppa())                # Kutsutaan kutonen funktiota nopan arvolla.
