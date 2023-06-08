import random

resp = input("Deseja jogar (SIM/NÃO? )")
while resp == "s" or resp == "S":
jog = random.randint(1,6)
comp = random.randint(1,6)
print("Jogador  : ", jog)
print("Computador  :", comp)
if jog > comp:
    print("Jogador ganhou!")
elif comp > jog:
    print("Computador ganhou!")
else:
    print("Empate!")