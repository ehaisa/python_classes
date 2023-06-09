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