#kokonaisluki, integer, INT
eka = -9

#kokonaisluku pitkä, long
toka = 12_456_123_180

#desimaaliluku, float
kolmas = 7.28

#kompleksiluku, complex
neljas = 3-2j


print(eka)
print(toka)
print(kolmas)
print(neljas)

pituus = int(input("Pituus: "))
paino = float(input("Paino: "))

#Muuttuja jossa laksu suoritetaan
bmi = paino / (pituus / 100) ** 2
print("pituus-paino-indeksi on", bmi)
print(f"BMI on {bmi:.2f}")