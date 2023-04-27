soma = 0
i = 1
while i <= 3:     # AQUI A QUANTIDADE DE NOTAS É LIMITADO PARA 3
    nota = float(input("Informe a nota %d: "% i))
    soma = soma + nota
    i = i + 1
media = soma / 3
print("Sua media foi: %.1f"% media)
if media >= 7.0:
    print("Parabéns! Você foi aprovado.")
else:
    print("Pena, você foi reprovado.")

    # ESTA VERSÃO CONTINUA FUNCIONANDO COM APENAS 3 NOTAS
    # A PARTIR DESTE PONTO É COMEÇADO A USAR A "FUNÇÃO" CHAMADA DE ACUMULADOR