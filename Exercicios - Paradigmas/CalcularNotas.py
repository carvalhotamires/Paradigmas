# Programa 01 - Linguagem Pyton
# Autor: Tamires Carvalho da Silva - Data: 18/08/2023 - Linguagem: Pyton
#Descrição Narrativa: Faça um progama que leia duas notas e calcule sua média e depois informe se o aluno foi aprovado ou reprovado dado que a média > = 7 para ser aprovado
# Leitura dos Dados de Entrada
def calmedia(n1, n2):
    return (n1 + n2) / 2

def verificarsituacao(med):
    if med >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Leitura dos Dados de Entrada
Nota1 = float(input("Informe o valor da primeira nota: "))
Nota2 = float(input("Informe o valor da segunda nota: "))

# Calcular a Média das Notas
med = calmedia(Nota1, Nota2)

# Estrutura de Decisão com IF para verificar se o aluno foi aprovado ou reprovado
resp = verificarsituacao(med)

# Escreva os resultados obtidos.
print("O valor da Média é:", med)
print("O conceito do Aluno foi:", resp)