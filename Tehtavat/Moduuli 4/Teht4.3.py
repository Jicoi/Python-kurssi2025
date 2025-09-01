#Tehtävä 4.3
#ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.


#kysytään lukuja.
luku = (input("Syötä luku: "))

#määritellään suurin ja pienin arvo.
suurin = int(luku)
pienin = int(luku)

#Määritetään että luvun täytyy olla eri kuin tyhjä. Vertaillaan arvojen suuruuksia.
while luku != "":
    print(luku)
    if int(luku) < pienin:
        pienin = int(luku)
    if int(luku) > suurin:
        suurin = int(luku)
    luku = (input("Syötä luku: "))

#Ilmoitetaan käyttäjälle pienin ja suurin arvo.
print(f"Pienin luku {pienin} ja suurin luku {suurin}")

