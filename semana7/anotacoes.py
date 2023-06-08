# na estrutura while, é obrigatóriamente false ou true
print("Contando de 1 até 10")
i = 1 # Inicialização
while i <= 10: # Teste
 print(i)
 i = i + 1 # Atualização
print("Fim do programa!")

# TESTE: em um programa que conta de 1 a 10, o critério de parada poderia ser a variável "contador"
# atingir o valor 11. A condição teste seria algo como "enquanto contador for menor ou igual a 10,
# continue executando o laço".

# INICIALIZAÇÃO: Antes de iniciar o laço de repetição,é necessário inicializar a variável que
# será utilizada no critério de parada com um valor adequado. (vem antes do while)

# ATUALIZAÇÃO: é importante atualizar a variável utilizada no critério de parada para garantir que,
# em algum momento, a condição teste se torne falsa e o laço seja interrompido