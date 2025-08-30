#Tehtävä 3.3

#kysytään sukupuoli ja hemoglobiiliarvo
bio = input("Syötä biologinen sukupuolesi: ").lower()
hemo = int(input("Syötä hemoglobiiniarvosi (g/l): "))

#Jos nainen kyseessä
if bio == "nainen" and hemo > 175:
    print("Hemoglobiinisi on korkea")
elif bio == "nainen" and hemo < 117:
    print("Hemoglobiinisi on matala")

#Jos vastaajana mies
elif bio == "mies" and hemo > 195:
    print("Hemoglobiinisi on korkea")
elif bio == "mies" and hemo < 134:
    print("Hemoglobiinisi on matala")

#Jos hemo osuu sukupuolien välillä annettuihin arvoihin tulostetaan "normaali"
else:
    print("Hemoglobiinisi on normaali")
