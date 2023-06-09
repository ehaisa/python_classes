#A cada partida, o programa deverá exibir o resultado de cada um dos dados e indicar
#quem foi o vencedor ou se houve empate
#Ao final da partida, o programa deve perguntar ao usuário se ele deseja jogar novamente.
#Caso ele opte por continuar o jogo, este deve ser executado novamente a partir do início
#Caso ele deseje encerrar a disputa, o programa deverá exibir o número de vitórias do jogador,
#o número de vitórias do computador e o número de empates

import random
Wjog = 0
Wcomp = 0
emp = 0
partidas = 0
resp = input("Deseja jogar (SIM/NÃO)? ")
while resp.lower() == "sim":          #o método 'lower()' permite que o usuário digite "sim" ou "SIM" sem distinção
    jog = random.randint(1, 6)
    comp = random.randint(1, 6)
    print("Jogador: ", jog)
    print("Computador: ", comp)
    if jog > comp:
        print("Jogador Ganhou!")
        Wjog += 1
    elif comp > jog:
        print("Computador Ganhou!")
        Wcomp += 1
    else:
        print("Empate!")
        emp += 1
    partidas += 1
    resp = input("Deseja jogar novamente (SIM/NÃO)? ")
print()
print("Jogo encerrado!")
print("Quantidade de partidas jogadas: ", partidas)
print("Placar Final")
print("--------------")
print("Jogador: ", Wjog)
print("Computador:", Wcomp)
print("Empates :", emp)
print("--------------")
print("Fim do Programa")