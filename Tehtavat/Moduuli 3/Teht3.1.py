#Tehtävä 3.1


#Kysytään kuhan mitta
kala = float(input("Kala on: "))


#Tehdään jos lauseke, joka vertaa pyydetyn kalan kokoa sallittuun mittaan.
if kala< 37:
    print(f"Päästä kala pois, kala on " f"{37 - kala}" " senttiä liian lyhyt")
else:
    print("voit pitää kalan")

