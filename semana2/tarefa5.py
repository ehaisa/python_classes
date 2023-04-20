import datetime

data = datetime.date.today()
ano_atual = data.year

print("Calcule a sua idade")

nome = input("Olá, qual o seu nome?")
ano_nasc = int(input("Em que ano você nasceu?"))

idade = ano_atual - ano_nasc
print("%s, o resultado final para a sua idade neste ano é %d anos"% (nome, idade))