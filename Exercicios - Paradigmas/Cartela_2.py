# Programa 11 - Linguagem Pyton
# Autor: Tamires Carvalho da Silva - Linguagem: Pyton
#Faça um programa em Python para gerar automaticamente
#números entre 0 e 99 de uma cartelar de bingo.
#Sabendo que cada cartela devera conter 5 linhas de 5 números,
#gere estes dados de modo a não ter números repetidos dentro das
# cartelas. O programa deve exibir na tela a cartela gerada.

import random

def main():
    cartela = random.sample(range(100), 25)  # Gera 25 números únicos entre 0 e 99
    print("Cartela de Bingo:")
    for i in range(5):
        print(cartela[i * 5 : (i + 1) * 5])

if __name__ == "__main__":
    main()
