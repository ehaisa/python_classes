#Array é uma estrutura de dados que pode armazenar uma coleção de elementos do mesmo tipo. Os arrays podem ter uma,
#duas ou mais dimensões, dependendo da quantidade de índices necessários para acessar um elemento específico.

# Array unidimensional
numeros = [1, 2, 3, 4, 5]
print(numeros[2])
#Para acessar cada elemento nesse caso: numeros[0] a numeros[4]

# Array bidimensional
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matriz[1][1])
#Para acessar cada elemento nesse caso: matriz[0][0], o primeiro índice indica a linha e o segundo indica o elemento.

# Array multidimensional
cubo = [[[1, 2], [3, 4]],
        [[5, 6], [7, 8]]]
print(cubo[1][0][0])
# pode ser acessado usando três índices: um para selecionar a "fatia", um para selecionar a linha e outro
# para selecionar a coluna.
# Por exemplo, cubo[1][0][0] retorna o primeiro elemento da primeira linha da segunda "fatia",que é 5.

#Vetores/arrays em Python são flexíveis, ou seja, o conjunto de índices não é fixo. Podem crescer ou diminuir durante
# a execução do programa sempre que um novo valor for adicionado ou retirado, além de poder conter elementos de tipos 
# diferentes. A estrutura de dados mais comum em Python é a "lista", alguns exemplo:

numeros = [1, 2, 3, 4, 5]  # Uma lista de números inteiros
nomes = ["João", "Marcela", "Pedro"]  # Uma lista de strings
agenda = ["Judite", 83999877654, 1.68, 69.3, "12/10/2002", "João Pessoa", True] # Lista com diferentes tipos de elementos

# PRÁTICA #

lista1 = []    # A lista é incialmente criada vazia, para armazenar dados depois.
print(lista1)
lista1 = lista1 + [10]     # Valor 10 é adicionado a ela
print(lista1)
lista1 += [20]    # Outra maneira de adição
print(lista1)
lista1.append(30) # O método append() adiciona um elemento ao final de uma lista existente
print(lista1)

# COMO ALTERAR UM ELEMENTO: usa-se vetor[elemento] = novo valor. Um exemplo:

vetor = [14, 37, 18, 92, 77, 64]
print("Lista original")
print(vetor)
vetor[0] = 99
print("Lista modificada")
print(vetor)
print("Elementos individuais")
print("Valor [0] =", vetor[0])
print("Valor [1] =", vetor[1])
print("Valor [2] =", vetor[2])
print("Valor [3] =", vetor[3])
print("Valor [4] =", vetor[4])
print("Valor [5] =", vetor[5])