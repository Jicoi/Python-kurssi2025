

# Tehdään funktio, joka laskee kokonaisluvut yhteen
def summaaja(kokonaisluvut):
    summa = 0
    for n in kokonaisluvut:         # käydään listan arvot läpi
        summa += n                  # lisätään summaan arvo
    print(summa)

# Tehdään funktio, joka luo listan 1-100 arvoille ja käyttää summaaja funktiotal laskeakseen arvot yhteen.
def paaohjelma():
    lista = []                      # luodaan lista
    for i in range(1, 101):         # syötetään listaan arvot 1-100 välillä
        print(i)
        lista.append(i)             # lisätään arvo listaan
    print(lista)
    summaaja(lista)


# Suoritetaan pääohjelma
paaohjelma()