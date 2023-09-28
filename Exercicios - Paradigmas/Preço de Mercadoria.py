# Programa 02 - Linguagem Pyton
# Autor: Tamires Carvalho da Silva - Data: 18/08/2023 - Linguagem: Pyton
#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
def valordodesconto(valor, desconto):
    return (valor * desconto) / 100
def precoapagar(preco, desconto):
    return preco - valordodesconto(preco, desconto)

preço = float(input("Digite o preço da mercadoria:"))
desconto = float(input("Digite o percentual de desconto:"))
valor_do_desconto = valordodesconto(preço, desconto)
a_pagar = precoapagar(preço, desconto)
print("Um desconto de %5.2f %% em uma mercadoria de R$ %7.2f" % (desconto, preço))
print("vale R$ %7.2f." % valor_do_desconto)
print("o valor a pagar é de R$ %7.2f" % a_pagar)