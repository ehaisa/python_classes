import datetime

data = datetime.date.today()
idade_limite = 60

nome = input("Olá! Qual o seu nome? ")
print("Seja bem-vindo(a).")

ano_nasc = int(input("Em que ano você nasceu?"))
ano_atual = data.year
idade = ano_atual - ano_nasc

if idade >= idade_limite:
    print("%s, este ano você completa %d anos! Já se vacinou contra a COVID?"% (nome, idade))
    print("Estou vendo aqui que já chegou na sua faixa etária")
    print("Se não tomou ainda, procure um posto de saúde")
else:
    print("%s, este ano você completa %d anos! Infelizmente ainda não chegou a sua vez para se vacinar."%(nome, idade))
    print("Por favor, fique atento(a) ao calendário de vacinação.")
print("Esperamos que tenha um bom dia!")