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