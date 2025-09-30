#Ohjelma, joka kysyy käyttäjältä tunnuksen ja salasanan. Vertaillaan ovatko tunnukset oikein.

#Asetetaan tunnus ja salasana
tunnus = ("pyhton")
salasana = ("rules")

#kysytään käyttäjältä tunnus ja salasana
kayttajantunnus = input("Anna käyttäjätunnus: ")
kayttajansalasana = input("Anna salasana: ")

#Asetetaan yrityksille ja tarkastukselle pohja
yritykset = 1
tarkastus = 0

#Vertaillaan käyttäjän syöttämiä tunnuksia ja lisätään kirjautumis yrtiksiin ja tarkastukseen +1,
#maksimi yrityksiä käyttäjällä on 5.
while yritykset < 5:
    if kayttajantunnus == "python":
        tarkastus += 1
    if kayttajansalasana == "rules":
        tarkastus += 1
    if tarkastus == 2:
        print("Tervetuloa!")
        exit(0)

#Kysytään aina uudelleen tunnukset jos ne on syötetty väärin. Lisätään kirjautumis yrtiksiin +1
    kayttajantunnus = input("Anna käyttäjätunnus: ")
    kayttajansalasana = input("Anna salasana: ")
    yritykset += 1
    print(yritykset)
print("Pääsy evätty")