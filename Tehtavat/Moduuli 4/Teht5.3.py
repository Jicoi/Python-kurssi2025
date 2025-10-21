#Ohjelma, joka kysyy kokonaislukua ja tarkastaa onko se true/false.


#Tehdään funktion, joka tarkastaa onko saatu arvo alkuluku.
def alkuluku(luku):
    if luku < 2:
        print("luku on alkuluku")
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            return False #en saanut toimimaan print("ei ole alkuluku")
    return True



#Kysytään lukua ja vertaillaan onko se alkuluku vai ei tai onko siinä vääriä merkkejä esim kirjaimia.
try:
    kayttajanluku = int(input("Syötä kokonaisluku: "))
    if alkuluku(kayttajanluku):
        print(f"luku {kayttajanluku} on alkuluku")
    else:
        print(f"luku {kayttajanluku} ei oel alkuluku")
except ValueError:
    print("Virheellinen arvo")

