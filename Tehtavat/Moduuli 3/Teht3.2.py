#Tehtävä 3.2
#ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen

#Kysytään asiakkaalta hänen hyttiään. Muutetaan asiakkaan syöttämä arvo aina isoksi kirjaimeksi.
hytti = input("Syötä hyttisi: ").upper()


#Tehdään vertailu arvolle, joka tulostaa asiakkaalle ohjeet.
if hytti == "LUX":
        print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "A":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B":
        print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
        print("C on ikkunaton hytti autokannen alapuolella.")
else:
        print("Virheellinen hyttiluokka.")

