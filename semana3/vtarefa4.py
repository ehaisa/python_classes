print("Cercando sua fazenda")

comp = float(input("Qual o comprimento, em metros, do terreno? "))
larg = float(input("Qual a largura, em metros, do terreno? "))

area = comp * larg
fios = 5 * area

print("A área total da fazenda é %.2f m²"% area)
print("O total de fios necessários são %.2f"% fios)