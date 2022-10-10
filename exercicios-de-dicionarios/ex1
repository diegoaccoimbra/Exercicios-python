#O programa ler nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final ele mostra: quantas pessoas foram cadastradas, a média de idade, uma lista com as mulheres e uma lista de pessoas com idade acima da média

dados = {}
pessoas = []
soma = 0
mulheres = []
acimaDaMedia = []

while True:
    dados["nome"] = input("\nNome: ")
    dados["sexo"] = input("Sexo: [M/F] ").upper()[0]
    dados["idade"] = int(input("Idade: "))

    pessoas.append(dados.copy())
    dados.clear()

    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]

        if resp not in "SN":
            continue
        else:
            break
    
    if resp in "N":
        break

print(dados)
print(pessoas)
print()
print(f"Foram cadastradas {len(pessoas)} pessoas")

for p in pessoas:
    soma = soma + p["idade"]

    if p["sexo"] == "F":
        mulheres.append(p["nome"])

media = soma / len(pessoas)
print(f"A média de idade foi {media:5.2f}")
print(f"As mulheres foram {mulheres}")

for p in pessoas:
    if p["idade"] > media:
        acimaDaMedia.append(p["nome"])

print(f"As pessoas que têm idade acima da média são {acimaDaMedia}")
