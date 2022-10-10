#O programa recebe 7 números inteiros e vai ordenar os números ímpares e pares em duas listas separadas que estão dentro de uma mesma lista.

numeros = [[], []]
maior = menor = 0

for i in range(0, 7):
    valor = int(input(f"Digite o {i+1}º valor: "))

    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()

print()
print(numeros)
