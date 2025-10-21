#Ohjelma, joka kysyy kaupungin nimiä yksitellen, tekee niistä listan ja toistaa ne syöttöjärjestyksessä.

#Tehdään lista johon nimet tallennetaan
kaupungit = []

#Kysytään käyttäjältä viisi kaupunkia
for i in range(5):                                           #range(5) koska halutaan vain 5 nimeä. (toistuu viisi kertaa)
    nimet = input(f"Syötä kaupunki ({i+1}/5): ")
    kaupungit.append(nimet)                                  #kaupungit.append lisää nimen listalle. (nimet)


#printataan kaupungit syötetyssä järjestyksessä
print("\nAntamasi kaupungit: ")                              #\n tekee uuden rivin seuraavalle syötteelle.
for kaupungit in kaupungit:                                  #luettelee listan kaupungit
    print(kaupungit)


