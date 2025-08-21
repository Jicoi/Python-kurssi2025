#Tehtävä 2.4

#Tarviinko edes tätä?? En tarvinnut, toimii ilmankin.
import math


#Kysytään arvot kolmelle luvulle
luku1 = float(input("luku1: "))
luku2 = float(input("luku2: "))
luku3 = float(input("luku3: "))

#Laskutoimitus ja tulostus lukujen summalle
summa = luku1 + luku2 + luku3
print(f"summa: {summa:.2f}")

#Laskutoimitus ja tulostus lukujen tulolle (kertolasku)
tulo = luku1 * luku2 * luku3
print(f"tulo: {tulo:.2f}")

#Keskiarvo luvuille tulostettuna
keskiarvo = summa / 3
print(f"keskiarvo: {keskiarvo:.2f}")



