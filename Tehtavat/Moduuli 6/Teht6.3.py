

# funktio, joka muuttaa gallonat litroiksi ja tulostaa muunnetun arvon.
def gallona_litraksi(gallona):
    litrat = int(gallona) * 3.785           # laskutoimitus litra muunnokselle.
    print(f"{litrat:.2f} litraa")


# funktion, joka kysyy käyttäjältä gallona määrän ja vertaa onko se hyväksyttävä arvo
def paaohjelma():
    gallona = input("Syötä gallonat: ")
    if int(gallona) < 0: exit()
    gallona_litraksi(gallona)               # kutsutaan muunnosfunktio paaohjelman sisälle.


# käynnistää paaohjelma funktion ja toistuu niin pitkään kunnes syötetään negatiivinen arvo
while True:
    paaohjelma()