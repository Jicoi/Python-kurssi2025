#Tehtävä 4.2
#Ohjelma, joka muuntaa tuumat senttimetreiksi jos luku ei ole negatiivinen


#Kysytään käyttäjältä arvo tuumissa.
tuumat = int(input("Tuumia: "))

#Vertaillaan tuumat arvoa onko se negatiivinen vai ei, toistetaan jos suurempi kuin 0 ja lopetetaan negatiivisella.
while tuumat >= 0: #Toiminto tarkastaa onko syötetty arvo positiivinen.

#Muutetaan syötetty arvo senttimetreiksi ja toistetaan arvon kysyntä jos luku ei ole negatiivinen.
    print(tuumat * 2.54, "cm")
    tuumat = int(input("Tuumia: "))

#Jos luku alle 0, toiminto loppuu.
print("Negatiivinen luku, toiminto lopetettu.")

