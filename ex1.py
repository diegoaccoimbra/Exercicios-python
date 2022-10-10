'''Cadastro de pessoas e seus respectivos pesos.
Os valores de nome e peso são dados e em seguida pergunta se a pessoa quer continuar a cadastrar pessoas. Os valores de cada pessoa (nome e peso) são guardados em uma lista que está dentro de uma lista que contém todas as pessoas.

No final o programa calcula o número de pessoas cadastradas e retorna os pesos e nomes da pessoa mais pesada e menos pesada respectivamente.
'''

lista = []
pessoa = []
maior = menor = 0

while True:
    pessoa.append(input("\nDigite o nome: "))
    pessoa.append(int(input("Digite o peso: ")))

    if len(lista) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]

    lista.append(pessoa[:])
    pessoa.clear()

    resposta = input("Quer continuar? [S/N]").upper()
    if resposta in "N":
        break
    else:
        continue

print("\n----------SAÍDA----------")
print(lista)

print(f"Foram cadastradas {len(lista)} pessoas")
print(f"O maior peso foi de {maior}Kg, peso de ", end="")
for p in lista:
    if p[1] == maior:
        print(f"[{p[0]}]", end=" ")
print(f"\nO menor peso foi de {menor}Kg, peso de ", end="")
for p in lista:
    if p[1] == menor:
        print(f"[{p[0]}]", end=" ")
