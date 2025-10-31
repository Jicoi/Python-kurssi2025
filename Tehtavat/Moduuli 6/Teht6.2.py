

import random

# Kysytään käyttäjältä arvo
maksimi = input("Anna maksimi arvo: ")

def noppa(maksimi):
    return random.randint(1, maksimi)       # haetaan arvo 1 - käyttäjän syöttämän arvon väliltä.


def kutonen(noppa):
    print(f"Heitto: {noppa}")
    if int(noppa) == int(maksimi):             # pysäyttää funktion kun ollaan saatu käyttäjän syöttämä arvo
        print(f"Maksimisi saatu!: {maksimi}")
        exit()


while True:
    kutonen(noppa(int(maksimi)))                # kutsutaan funktiota kutonen ja sen sisään annetaan -
                                                # - funktio noppa, joka käyttää arvoa maksimi