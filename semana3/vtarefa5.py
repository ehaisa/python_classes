print("Geometricamente falando")
print("calculadora para trapézio, losango e circulo")
print()

print("CALCULO DO TRAPÉZIO")

bMaior = float(input("Defina um valor para a base maior: "))
bMenor = float(input("Defina um valor para a base menor: "))
altura = float(input("Defina um valor para a altura: "))

areaT = (bMaior + bMenor) * altura / 2
print("A area do trapézio é %.2f"% areaT)
print()

print("CALCULO DO LOSANGO")

dMaior = float(input("Defina um valor para a diagonal maior: "))
dMenor = float(input("Defina um valor para a diagonal menor: "))

areaL = (dMaior * dMenor) / 2
print("A area do losango é %.2f"% areaL)
print()

print("CALCULO DO CIRCULO")

raio = float(input("Defina um valor para o raio: "))

areaC = 3.14 * raio ** 2
perimentoC = 2 * 3.14 * raio

print("A area do circulo é %.2f"% areaC)
print("O perimentro do circulo é %.2f"% perimentoC)