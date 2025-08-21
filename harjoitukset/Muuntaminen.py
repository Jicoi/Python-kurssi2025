#Muuntaminen, tapa 1

ika_str = input("Kuinka vanha olet?: ")
ika = int(ika_str)

print("eli olet syntynyt", 2025-ika)


#Muuntaminen, tapa 2
ika = int(input("Kuinka vanha olet?: "))

print("olet syntynyt", str(2025-ika) +".")

#muotoiltu tuloste
print(f"ai olet syntynyt {2025-ika}.")
