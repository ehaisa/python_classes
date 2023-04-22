print("Olá, boas vindas ao comparador de idades!")

user1 = input("Qual o nome do usuário 1? ")
user2 = input("E qual o nome do usuário 2? ")
idade1 = int(input("Por favor, %s, nos informe a sua idade: "% user1))
idade2 = int(input("%s, agora nos informe a sua idade: "% user2))

if idade1 > idade2:
    print(user1, "é mais velho(a) que", user2)
elif idade1 == idade2:
    print("Me parece que ambos vocês tem a mesma idade.")
else:
    print(user2, "é mais velho(a) que", user1)