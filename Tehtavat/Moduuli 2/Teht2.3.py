#Tehtävä 2.3

#kysytään arvot kannalle ja korkeudelle
kanta = float(input("Kanta: "))
korkeus = float(input("Korkeus: "))


#laskutoimitukset
pinta_ala = kanta * korkeus
piiri = 2 * (kanta + korkeus)


#tulostetaan luvut
print(f"piiri on {piiri:.2f} ")
print(f"pinta-ala on {pinta_ala:.2f} ")

