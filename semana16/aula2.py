import random
def exibe_mensagem(nome):
    print("Bom dia, Prof. %s!"%nome)
    print("Seja bem vindo.")
    print("Esperamos que goste do nosso programa...")

def sorteia_aluno(a, b):
    x = random.randint(a, b)
    return x

## Programa principal
nome = input("Qual o seu nome? ")
exibe_mensagem(nome)
qde = int(input("Quantos alunos tem na sua turma? "))
x = sorteia_aluno(1, qde)
print("Aluno sorteado: ", x)