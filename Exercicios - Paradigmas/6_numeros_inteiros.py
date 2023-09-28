# Programa 10 - Linguagem Pyton
# Autor: Tamires Carvalho da Silva - Linguagem: Pyton
# Faça um programa em Python que receba 6 numeros inteiros e mostre;
#  • Os numeros pares digitados; 
#  • A soma dos numeros pares digitados; 
#  • Os numeros   ımpares digitados;
#  • A quantidade de numeros  ımpares.

def main():
    numeros_pares = []
    numeros_impares = []

    for _ in range(6):
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            numeros_pares.append(numero)
        else:
            numeros_impares.append(numero)

    print("Os números pares digitados são:", numeros_pares)
    print("A soma dos números pares digitados é:", sum(numeros_pares))

    print("Os números ímpares digitados são:", numeros_impares)
    print("A quantidade de números ímpares digitados é:", len(numeros_impares))

if __name__ == "__main__":
    main()
