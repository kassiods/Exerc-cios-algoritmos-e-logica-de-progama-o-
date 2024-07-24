'''
Escreva um programa que cria uma lista de duas dicmensões uTlizando List
Comprehsion e imprima a diagonal principal desta lista.
'''

lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# Cria uma matriz 3x3 preenchida com números inteiros inseridos pelo usuário
a = [[int(input(f"Digite um numero: ")) for j in range(3)] for i in range(3)]

# Inicializa uma lista vazia para armazenar os elementos da diagonal principal
dp = []

# Percorre cada linha da matriz
for i in range(3):
    # Percorre cada coluna da matriz
    for j in range(3):
        # Verifica se o índice da linha é igual ao índice da coluna (elemento da diagonal principal)
        if i == j:
            # Armazena o elemento da diagonal principal
            d = a[i][i]
            # Adiciona o elemento à lista dp
            dp.append(d)

# Exibe os elementos da diagonal principal
print(f"Diagonal principal: {dp}")