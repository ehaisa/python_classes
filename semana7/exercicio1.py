n1 = int(input("Informe a 1a. nota: "))
n2 = int(input("Informe a 2a. nota: "))
n3 = int(input("Informe a 3a. nota:"))

media = (n1 + n2 + n3) / 3
print("Sua media foi: %.1f"% media)

if media >= 7.0:
    print("Parabéns! Você foi aprovado")
else:
    print("Pena, você foi reprovado!")

    # ESTA VERSÃO ESTÁ ERRADA, POIS NOTAS SÃO DE VALOR FLOAT, NÃO INT
    # ELA TAMBÉM SÓ IRÁ FUNCIONAR COM APENAS 3 NOTAS
#############################################################################################################
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
#############################################################################################################
soma = 0
i = 1
n = int(input("Informe quantas notas você quer calcular: "))
while i <= n:
    nota = float(input("Infome a nota %d: "%i))
    soma = soma + nota
    i = i + 1            # ATUALIZAÇÃO: quando o laço é finalizado, o valor de i aumenta +1 e para ao checar no valor de n
media = soma/n
print("Sua média foi %.1f"%media)
if media >= 5.0:
    print("Parabéns! Você foi aprovado!")
else:
    print("Pena, você foi reprovado!")
print("Fim do Programa")

# Esse programa serve para qualquer quantidade de notas