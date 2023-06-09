temp = []
print("Programa Temperaturas")

for i in range(6):
  t = float(input("Digite a temperatura %d: "%(i+1)))
  temp = temp + [t]

print()
print("Lista de Temperaturas")
for i in range(6):
  print("Valor %d: %.1fºC"%(i+1, temp[i]))

print()
print("Lista de Temperaturas Invertida")
for i in range(5, -1, -1):
  print("Valor %d: %.1fºC"%(i+1, temp[i]))

temp.sort()
print(temp)
temp.sort(reverse=True)
print(temp)

tam = len(temp)
for i in range(tam-1):
  for j in range(i+1, tam):
    if temp[i] > temp[j]:
      aux = temp[i]
      temp[i] = temp[j]
      temp[j] = aux
print("Lista Ordenada")
print(temp)