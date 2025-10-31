


# Tehdään funktio, joka lisää parilliset omaan listaan
def summaaja(kokonaisluvut):
    parilliset = []
    for n in kokonaisluvut:         # käydään listan arvot läpi
        if n % 2 == 0:              # tarkastetaan onko luku parillinen
            parilliset.append(n)
    return parilliset


# Tehdään funktio, joka luo listan 1-100 arvoille ja erottelee listat alkuperäiseksi ja parillisiksi.
def paaohjelma():
    lista = []                      # luodaan lista
    for i in range(1, 101):         # syötetään listaan arvot 1-100 välillä
        lista.append(i)             # lisätään arvo listaan
    print("Parilliset:", summaaja(lista))
    print(f"Alkuperäinen lista:", lista)


# Suoritetaan pääohjelma
paaohjelma()