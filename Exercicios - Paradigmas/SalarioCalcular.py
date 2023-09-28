# Programa 04 - Linguagem Pyton
# Autor: Tamires Carvalho da Silva - Data: 18/08/2023 - Linguagem: Pyton
#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um amumento de 10%. Para os inferiores ou iguais, de 15%.
salário = float(input("Digite seu salário: "))
pc_aumento = 0.15
if salário > 1250:
  pc_aumento = 0.10
aumento = salário * pc_aumento

print(f"Seu aumento será de: R$ {aumento:7.2f}")
print(f"o percentual de aumento foi: {pc_aumento:7.2f}")
salárionovo = salário + aumento
print(salárionovo)

#Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
#Esse valor será depositado no início de cada mês,
#e você deve considerá-lo para o cálculo de juros do mês seguinte.

depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
investimento = float(input("Depósito mensal: "))
mês = 1
saldo = depósito
while mês <= 24:
    saldo = saldo + (saldo * (taxa/ 100)) + investimento
    print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
    mês = mês + 1
print(f"O ganho obitido com os juros foi de R${saldo-depósito:8.2f}.")

# 5.2f e 8.2f são formatações para escolher a quantidade de caracteres (5 e 8) e
# a quantidade de nnúmeros após a vírgula (.2f).