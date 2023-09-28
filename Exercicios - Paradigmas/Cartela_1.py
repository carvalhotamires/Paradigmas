# Programa 11 - Linguagem Pyton
# Autor: Tamires Carvalho da Silva - Linguagem: Pyton
# Faça um programa em Pyton para gerar automaticamente
# numeros entre 0 e 99 de uma cartela de bingo.
# Sabendo que cada cartela devera conter 5 linhas de 5 numeros,
# das cartelas. O programa deve exibir na
# tela a cartela gerada.

import random

def gerar_cartela():
    cartela = []

    while len(cartela) < 25:
        numero = random.randint(0, 99)
        if numero not in cartela:
            cartela.append(numero)

    return cartela

def exibir_cartela(cartela):
    for i in range(5):
        for j in range(5):
            index = i * 5 + j
            print(f'{cartela[index]:2}', end='  ')
        print()

def main():
    num_cartelas = int(input("Quantas cartelas você deseja gerar? "))

    for i in range(num_cartelas):
        cartela = gerar_cartela()
        print(f'\nCartela {i + 1}:\n')
        exibir_cartela(cartela)

if __name__ == "__main__":
    main()