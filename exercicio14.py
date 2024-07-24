'''
Escreva um programa que encontre os números primos é uma tarefa
difícil. Faça um programa que gera uma lista dos números primos
existentes entre 1 e um número inteiro informado pelo usuário.
'''

# Pergunta ao usuário o número limite e converte a entrada para um número inteiro (int)
limite = int(input("Digite um número inteiro: "))

# Inicializa uma lista vazia para armazenar os números primos encontrados
primos = []

# Percorre todos os números a partir de 2 até o número limite (1 não é considerado primo)
for num in range(2, limite + 1):
    # Assume inicialmente que o número é primo
    is_primo = True
    # Verifica se o número é divisível por algum número menor que ele, até a raiz quadrada do número
    # Não é necessário verificar além da raiz quadrada, pois os fatores se repetem
    for i in range(2, int(num**0.5) + 1):
        # Se o número for divisível por i, então não é primo
        if num % i == 0:
            is_primo = False
            break
    # Se o número não foi marcado como não primo, adiciona à lista de números primos
    if is_primo:
        primos.append(num)

# Exibe a lista de números primos encontrados entre 1 e o número limite
print("Números primos entre 1 e", limite, "são:", primos)
