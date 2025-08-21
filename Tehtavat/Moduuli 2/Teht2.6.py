#Tehtävä 2.6

#Tuodaan random kirjasto
import random

#Haetaan kolme eri satunnaista lukua 0 - 9 väliltä
luku1 = (random.randint(0,9))
luku2 = (random.randint(0,9))
luku3 = (random.randint(0,9))

#Tulostetaan satunnainen kolminumeroinen koodi.
print(f"Koodi on: {luku1} {luku2} {luku3}")



#nelinumeroinen koodi 1-6 väliltä
koodi1 = (random.randint(1,6))
koodi2 = (random.randint(1,6))
koodi3 = (random.randint(1,6))
koodi4 = (random.randint(1,6))

#Tulostetaan satunnainen nelinumeroinen koodi.
print(f"Koodi on: {koodi1} {koodi2} {koodi3} {koodi4}")

