leiviskat = float(input("Massa leivisköinä?: "))

naulat = float(input("Massa nauloina?: "))

luodit = float(input("Massa luoteina?: "))


leiviskat_grammoina = leiviskat*20*32*13.3
naulat_grammoina = naulat*32*13.3
luodit_grammoina = luodit*13.3

massa = leiviskat_grammoina + naulat_grammoina + luodit_grammoina

print(f"Massa nykyajassa: {massa:.2f}")
