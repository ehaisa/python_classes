#A estrutura for é usada para ações repetitivas dentro do código.
#Todo for, é um "for each", ou seja, é a execução de um código para cada item de um conjunto

#Percorrer uma lista/calcular imposto sobre diversos itens
lista_precos = (11, 20, 32, 45, 50)
for preco in lista_precos:
    imposto = preco * 0.1
    print("Preço:")
    print(imposto)
#Percorrer dicionário
produtos = {
    "maçã": 1,
    "cereal": 2,
    "leite": 3,
    "detergente": 4,
    "perfume": 5
}
for item in produtos:
    print(item.capitalize())                 #A função capitalize coloca a primeira letra de cada item em maiúscula
    print(produtos[item])
    print("-----  -----")


#Range: estrutura que define a quantidade de vezes que o for irá repetir, excluindo o último número.

for i in range(5):
    print(i)        #Ao executar, percebe que a variável vai até o 4, por que? Pois ela começa do 0, então o range não faz
                    #uma contagem de números, mas a quantidade, em resumo, de 0 até 4, são 5 repetições.