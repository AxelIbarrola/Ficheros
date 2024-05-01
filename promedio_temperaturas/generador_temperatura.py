# Genero de forma aleatoria las 31 temperaturas correspondientes a los 12 meses
from random import randint

for mes in range(12):
    print("")
    for temperatura in range(31):
        print(randint(5, 35), end=" ")