i = 1
soma = 0
n = int(input("Quantas notas? "))  # AO SETAR UMA VARIÁVEL COM INPUT, O PROGRAMA NÃO LIMITA UMA QUANTIDADE DE NOTAS
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

    # A PARTIR DESSA VERSÃO, O PROGRAMA PASSA A FUNCIONAR COM A QUANTIDADE DE NOTAS QUE O USUÁRIO QUISER, OU SEJA, N VEZES