'''
Escreva um programa que cria uma lista de duas dicmensões uTlizando List
Comprehsion e imprima a diagonal principal desta lista.
'''

lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# Imprimindo a diagonal principal da lista
# Usando uma List Comprehension para extrair a diagonal principal:
# range(len(lista)) gera uma sequência de índices de 0 até o comprimento da lista menos 1.
# lista[i][i] acessa o elemento na posição [i][i] da matriz.
# for i in range(len(lista)) percorre sobre cada índice e seleciona o elemento correspondente da diagonal principal.
diagonal_principal = [lista[i][i] for i in range(len(lista))]
print(diagonal_principal)