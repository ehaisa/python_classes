comprimento = float(input("Informe o comprimento (em metros): "))
largura = float(input("Informe a largura (em metros): "))
altura = float(input("Informe a altura (em metros): "))

area1 = comprimento * largura
area2 = largura * altura
area3 = altura * comprimento

area_total = area1 + (2 * area2) + (2 * area3)

print("O valor da área total a ser pintada é %.2f m²"% area_total)