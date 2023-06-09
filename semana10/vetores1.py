import random

cartao = []
print("Programa Mega Sena Milionária")
cont = 0
numDez = int(input("Quantas dezenas deseja marcar (6~10)? "))
while cont < numDez:
  valor = random.randint(1,60)
  if valor not in cartao:
    cartao = cartao + [valor]
    cont += 1
print()
cartao.sort()
print("O seu cartão de apostas foi gerado:")
for i in range(numDez):
  print(cartao[i], end=" ")
print()
print("Boa sorte!")