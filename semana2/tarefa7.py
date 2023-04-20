nome = input("Olá, qual o seu nome? ")
a_m = float(input("%s, qual a sua altura? "% nome))
a_cm = a_m * 100

peso_h = (a_cm - 100) - (a_cm - 150) / 4
peso_m = (a_cm - 100) - (a_cm - 150) / 2

print("%s, seu peso ideal para homem é %.2f"% (nome, peso_h))
print("E seu peso ideal para mulher é %.2f"%peso_m)