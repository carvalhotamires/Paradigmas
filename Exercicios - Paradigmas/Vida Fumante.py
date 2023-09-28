# Programa 03 - Linguagem Pyton
# Autor: Tamires Carvalho da Silva - Data: 18/08/2023 - Linguagem: Pyton
#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fuamte perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

# Redução do tempo de vida
def tempodevida (tempodevida) :
  return anos_fumando * 365 * cigarros_por_dia * 10
# Leitura de Dados
cigarros_por_dia = int(input("Quantidadde de cigarros por dia:"))
anos_fumando = float(input("Quantidade de anos fumando:"))
redução_em_minutos = tempodevida(tempodevida)

# Um dia tem 24 x 60 minutos
redução_em_dias = redução_em_minutos / (24 * 60)
valor_em_anos = redução_em_dias / 365
print("Redução do tempo de vida %8.2f dias." % redução_em_dias)
print("Valor em anos:", valor_em_anos)