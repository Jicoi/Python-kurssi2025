#Ympyrän säde

#haetaan pythonin matematiikka kirjasto
import math

#seuraavaksi kysytään säde ja tehdään siitä desimaaliluku
sade = float(input("Kerro ympyrän säde: "))

#sitten tehdään laskuri pinta-alalle ja haetaan matikka kirjastosta pi:n kaava (pi x r^2)
pinta_ala = math.pi * sade ** 2

#lopuksi haetaan tulos
print(f"Ympyrän pinta-ala on {pinta_ala:.2f}")

