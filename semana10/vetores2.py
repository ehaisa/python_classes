temp = []
print("Programa Temperaturas")

for i in range(6):
  t = float(input("Digite a temperatura %d: "%(i+1)))
  temp += [t]

print()
print("Lista de Temperaturas")
for i in range(6):
  print("Valor %d: %.1fºC"%(i+1, temp[i]))

print()
print("Lista de Temperaturas Invertida")   # O '5' indica valor inicial do loop, ou seja, o loop começará pelo sexto elemento.
for i in range(5, -1, -1):                 # O primeiro '-1' é o valor final, é usado para indicar que o loop deve percorrer
  print("Valor %d: %.1fºC"%(i+1, temp[i])) # até o primeiro elemento, contando de trás para frente. O segundo '-1' decrementa
                                           #o valor de i em 1 a cada iteração, ou seja, percorrre os elementos de forma decrescente.
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


# temp.sort(): Esse método é usado para ordenar a lista temp em ordem crescente. 
