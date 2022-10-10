#Programa que gerencia o aproveitamento de vários jogadores de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. Após isso o programa pergunta se o usuário quer continuar a cadastrar jogadores. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato, para cada jogador. Cada dicionário de umjogador é armazenado numa lista que contém todos os jogadores. No final o programa pergunta se o usuário quer ver dados de um determinado jogador.

jogador = {}
time = []

while True:
    cont = 0
    listaGols = []
    totalGols = 0
    jogador["nome"] = input("\nNome do jogador: ")

    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    while cont != partidas:
        numGols = int(input(f"Quantos gols na partida {cont+1} ? "))
        listaGols.append(numGols)
        totalGols = totalGols + numGols
        cont = cont + 1

    jogador["gols"] = listaGols
    jogador["total"] = totalGols

    time.append(jogador.copy())
    jogador.clear()

    while True:
        resp = input("Quer continuar? [S/N] ").upper()
        if resp not in "SN":
            continue
        else:
            break
    if resp in "N":
        break

print("-"*50)
print(time)
print("-"*50)
print(f"{'Código':>5} {'Nome':>10} {'Gols':>10} {'Total':>10}")

for i, j in enumerate(time):
    print(i, j["nome"], j["gols"], j["total"])

print("-"*50)

while True:
    dadojogador = int(input("\nMostrar dados de qual jogador? (Digite 999 para parar) "))

    for i, j in enumerate(time):
        if i == dadojogador:
            print(f"Levantamento do jogador {j['nome']}")
            for ind, gol in enumerate(j["gols"]):  
                print(f"No jogo {ind+1} fez {gol} gols")
    
    if dadojogador == 999:
        break

print("\nPROGRAMA FINALIZADO")
