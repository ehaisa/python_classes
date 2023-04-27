i = 1
soma = 0
n = int(input("Quantas notas? "))
while i <= n:
    nota = float(input("Informe a nota: "))
    soma = soma + nota
    i = i + 1
media = soma / n
print("Sua média foi: %.1f"% media)
if media >= 7.0:
    print("Parabéns! Você foi aprovado!")
else:
    print("Pena... você foi reprovado.")