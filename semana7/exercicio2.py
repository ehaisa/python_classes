from random import randint
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
print("Fim do Programa")