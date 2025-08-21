#Tehtävä 2.5

#Kysytään massat
leiviskat = float(input("Massa leivisköinä?: "))
naulat = float(input("Massa nauloina?: "))
luodit = float(input("Massa luoteina?: "))

#Muutetaan massat grammoiksi
leiviskat_grammoina = leiviskat*20*32*13.3
naulat_grammoina = naulat*32*13.3
luodit_grammoina = luodit*13.3

#Laskutoimitus massoille (grammoina)
massa = leiviskat_grammoina + naulat_grammoina + luodit_grammoina

#Erotellaan massa kiloiksi ja grammoiksi. Poistetaan kilon takaa ylimääräinen desimaali.
kiloina = int(massa / 1000)
grammoina = massa % 1000

#Tulostetaan massa
print(f"Massa nykyajassa:\n{kiloina} kiloa ja {grammoina:.2f} grammaa.  ")

