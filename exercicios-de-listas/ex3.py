#Gerador de jogos diferentes para mega sena a partir de uma quantidade dada pelo usuário.

from random import randint
from time import sleep

lista = []
jogos = []
cont2 = 0

QtdJogos = int(input("\nQuantos jogos você quer? "))

while cont2 != QtdJogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont = cont + 1
        if cont >= 6:
            break
        
    cont2 = cont2 + 1

    lista.sort()
    jogos.append(lista[:])
    lista.clear()


print(f"\n{QtdJogos} jogos sorteados:")
for indice, jogo in enumerate(jogos):
    print(f"{indice+1}º jogo: {jogo}")
    sleep(0.5)
print("\nJogos sorteados!")
