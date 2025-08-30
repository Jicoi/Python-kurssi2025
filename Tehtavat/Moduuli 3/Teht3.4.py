#Tehtävä 3.4

#Kysytään käyttäjältä vuosilukua.
vuosi = int(input("Anna vuosiluku: "))


#Vertaillaan onko vuosi jaollinen 4:llä tai 400:lla ja printataan käyttäjälle vastaus.
if vuosi % 4 == 0 or vuosi % 400 == 0:
    print(f"{vuosi} on karkausvuosi")
else:
    print(f"{vuosi} ei ole karkausvuosi")

