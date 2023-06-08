from random import randint  # ESTE COMANDO IMPORTA APENAS UM COMANDO ESPECÍFICO, NÃO A BIBLIOTECA INTEIRA

p = int(input('Quantas partidas você quer jogar? '))
i = 1
while i <= p:
    print("Partida no.", i)
    jog = int(input("Escolha 1 p/Cara e 2 p/Coroa: "))
    moeda = randint(1,2)
    if (jog == 1) and (moeda == 1):
        print("Deu Cara! Parabéns, você ganhou.")
    elif (jog == 1) and (moeda == 2):
        print("Deu Coroa! Infelizmente, você perdeu.")
    elif (jog == 2) and (moeda == 2):
        print("Deu Coroa! Parabéns, você ganhou.")
    else:
        print("Deu Cara! Infelizmente, você perdeu.")
    i = i + 1
    print()
    print("Fim do programa.")