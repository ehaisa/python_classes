import datetime

ano = int(input("Qual ano você quer testar? "))

if (ano % 4 == 0) and (ano % 100 != 0):
    print(ano, "é bissexto.")
elif (ano % 400 == 0):
    print(ano, "é bissexto")
else:
    print(ano, "não é bissexto")