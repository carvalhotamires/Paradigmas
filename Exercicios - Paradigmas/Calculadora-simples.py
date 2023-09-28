# Crie uma calculadora simples em Python
# Função para realizar a operação de adição
def adicao(x, y):
    return x + y

# Função para realizar a operação de subtração
def subtracao(x, y):
    return x - y

# Função para realizar a operação de multiplicação
def multiplicacao(x, y):
    return x * y

# Função para realizar a operação de divisão
def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero"
    return x / y

while True:
    print("Opções:")
    print("Digite 'sair' para encerrar o programa")
    print("Digite 'adicionar' para somar")
    print("Digite 'subtrair' para subtrair")
    print("Digite 'multiplicar' para multiplicar")
    print("Digite 'dividir' para dividir")

    escolha = input(": ")

    if escolha == "sair":
        break

    if escolha in ("adicionar", "subtrair", "multiplicar", "dividir"):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == "adicionar":
            print("Resultado:", adicao(num1, num2))
        elif escolha == "subtrair":
            print("Resultado:", subtracao(num1, num2))
        elif escolha == "multiplicar":
            print("Resultado:", multiplicacao(num1, num2))
        elif escolha == "dividir":
            print("Resultado:", divisao(num1, num2))
    else:
        print("Escolha inválida. Tente novamente.")
