print("Descobrindo diferença de idades")
print("Olá, sejam bem vindos(as)!")

user1 = input("Qual o nome do usuário 1? ")
user2 = input("E qual o nome do usuário 2? ")

idade1 = int(input("Por favor, %s, nos informe a sua idade: "% user1))
idade2 = int(input("%s, agora nos informe a sua idade: "% user2))

if idade1 > idade2:
    dif = idade1 - idade2
    print("A diferença de idade de vocês é de %d anos"% dif)
elif idade2 > idade1:
    dif = idade2 - idade1
    print("A diferença de idade de vocês é de %d anos"% dif)
else:
    print("Vocês possuem a mesma idade.")