# se usa o return no def, quando tiver alguma variável. O return retorna o valor para quem o chamou.Exemplo:
import random
def sorteia_aluno():   # definiu a função
    x = random.randint(1,50)    # definiu a variável
    return x    # mostra o valor sorteado no programa principal
##Programa principal
x = sorteia_aluno()
print("Aluno sorteado: ",x)


def sorteia_aluno(qde):   # qde irá esperar um valor do chamador, para retornar o valor
    x = random.randint(1,qde)
    return x
##Programa principal
num_max = int(input("Quantos alunos? "))
aluno = sorteia_aluno(num_max)
print("Aluno sorteado: ",aluno)