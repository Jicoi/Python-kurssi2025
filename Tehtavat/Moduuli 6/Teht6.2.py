

import random

# Kysytään käyttäjältä arvo
maksimi = input("Anna maksimi arvo: ")


def noppa(maksimi):
    return random.randint(1, maksimi)       # haetaan arvo 1 - käyttäjän syöttämän arvon väliltä.


def kutonen(noppa, kierrokset):
    print(f"Heitto: {noppa}")
    if int(noppa) == int(maksimi):             # pysäyttää funktion kun ollaan saatu käyttäjän syöttämä arvo
        print(f"Maksimisi saatu!: {maksimi}. Sinulla meni {kierrokset} kierrosta")
        exit()

kierrokset = 0

while True:
    kierrokset += 1
    kutonen(noppa(int(maksimi)), kierrokset)                # kutsutaan funktiota kutonen ja sen sisään annetaan -
                                                # - funktio noppa, joka käyttää arvoa maksimi

    # testi mielessä kokeilin lisätä laskurin heitetyille kierroksille.