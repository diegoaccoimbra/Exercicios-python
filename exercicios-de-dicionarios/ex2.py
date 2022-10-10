#Jogo de dados aleatórios com ranking dos jogadores a partir de qual tirou o maior valor

from random import randint
from operator import itemgetter
from time import sleep
d = {}
ranking = []

d["jogador1"] = randint(1, 6)
d["jogador2"] = randint(1, 6)
d["jogador3"] = randint(1, 6)
d["jogador4"] = randint(1, 6)

for jogador, valor in d.items():
    print(f"{jogador} tirou {valor} no dado")
    sleep(0.5)

ranking = sorted(d.items(), key=itemgetter(1), reverse=True)

print(ranking)
print("\n--------------------RANKING--------------------")

for j, v in enumerate(ranking):
    print(f"{j+1}º lugar: {v[0]} com {v[1]} tirado no dado")
