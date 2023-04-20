print("Calcule a sua idade")

nome = input("Olá, qual o seu nome?")
ano_nasc = int(input("Em que ano você nasceu?"))
ano_atual = int(input("Qual ano gostaria de usar?"))

idade = ano_atual - ano_nasc
print("%s, neste ano você completa %d anos"% (nome, idade))