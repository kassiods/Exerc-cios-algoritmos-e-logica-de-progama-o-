# Faça um programa que calcule o fatorial de todos os numeros impares 
# dentre os 10 primeiros da sequência de Fibonacci.


# Definindo a sequência de Fibonacci como uma tupla
fibonacci = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55)

# Passando por cada número na sequência de Fibonacci
for i in fibonacci:
    # Verificando se o número é ímpar
    if i % 2 != 0:
        # Inicializando a variável fatorial com 1
        fatorial = 1
        # Calculando o fatorial do número ímpar
        for j in range(1, i + 1):
            fatorial *= j
        # Imprimindo o fatorial do número ímpar
        print(fatorial)
        