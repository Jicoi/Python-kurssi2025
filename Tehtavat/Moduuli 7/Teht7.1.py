# Ohjelma, joka kysyy kuukauden numeron ja tulostaa sen vuodenajan

# kysytään käyttäjältä kuukauden numero
kuunnro = int(input("Syötä kuukauden numero: "))


# määritellään vuodenajat kuukausille.
vuodenajat = (
    "talvi", # joulukuu/12
    "talvi", # tammikuu/1
    "talvi", # helmikuu/2
    "kevät", # maaliskuu/3
    "kevät", # huhtikuu/4
    "kevät", # toukokuu/5
    "kesä", # kesäkuu/6
    "kesä", # heinäkuu/7
    "kesä", # elokuu/8
    "syksy", # syyskuu/9
    "syksy", # lokauu/10
    "syksy" # marraskuu/11
)

# tulostetaan käyttäjälle kuukauden numeroa vastaava vuodenaika.
print("Vuodenaika on:", vuodenajat[kuunnro % 12])

