print("Planeje seu terreno")
print("versão de área triangular")
print("Precisando descobrir a área para construir sua casa? Podemos ajudar!")

nome = input("Qual o seu nome? ")
print("Olá, %s, seja bem vindo!"% nome)

base = float(input("Por favor, nos informe o valor da base (em metros): "))
largura = float(input("E qual o valor da largura? (em metros) "))

area = (base * largura) / 2

print("A área total de seu terreno é de %.2f m²"% area)