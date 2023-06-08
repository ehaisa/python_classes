#O usuário deverá escolher entre Cara ou Coroa
#➢ O computador será responsável por jogar a moeda (sorteia valor entre 1 e 2)
#➢ Se o valor sorteado for igual ao valor que o usuário escolheu, ele ganha o jogo. Se for diferente, ele perde
#➢ Adicione um laço (estrutura de repetição) que permita ao usuário jogar várias vezes

from random import randint
p = int(input("Quantas partidas você quer jogar? "))
i = 1
while i <= p:
 print("Partinda no. %d "%i)
 jog = int(input("Escolha 1 p/ Cara ou 2 p/ Coroa: "))
 moeda = randint(1,2)
 if (jog == 1) and (moeda == 1):
  print("Deu Cara, você ganhou!")
 elif (jog == 1) and (moeda == 2):
  print("Deu Coroa, você perdeu!")
 elif (jog == 2) and (moeda == 2):
  print("Deu Coroa, você ganhou!")
 else:
  print("Deu Cara, você perdeu!")
 i = i + 1
 print()
print("Fim do Programa")