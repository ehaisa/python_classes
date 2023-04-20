print("Conversor de temperatura")

nome = input("Olá, qual é o seu nome?")
temp_c = int(input("Qual a temperatura atual em Celsius? "))

temp_f = (temp_c * 9/5) + 32

print("%s, hoje está fazendo %.2f graus Fahrenheit"% (nome, temp_f))