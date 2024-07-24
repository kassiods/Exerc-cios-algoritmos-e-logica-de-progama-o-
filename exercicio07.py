'''
Escreva um programa em python que leia um lista de 20 inteiros, calcule e
imprima:
a. A moda dos elementos na lista (elemento mais freqüente).
b. A mediana dos elementos no array (elemento central)
c. A média.
'''

# Inicializa um dicionário para contar a ocorrência de cada número
contador = {}

# Cria uma lista de números de 1 a 20
lista_numeros = list(range(1, 21))

# Conta a ocorrência de cada número na lista
for numero in lista_numeros:
    if numero in contador:
        # Se o número já estiver no dicionário, incrementa a contagem
        contador[numero] += 1
    else:
        # Se o número não estiver no dicionário, adiciona com contagem 1
        contador[numero] = 1

# Inicializa variáveis para encontrar a moda
moda = None
max_count = 0

# Encontra o número que mais aparece na lista (a moda)
for numero, count in contador.items():
    if count > max_count:
        # Atualiza a moda e o máximo de contagem
        moda = numero
        max_count = count

# Imprime o número que mais aparece na lista
print("A moda dos elementos na lista é:", moda)

# Calcula a mediana
# Ordena a lista de números
lista_ordenada = sorted(lista_numeros)
tamanho = len(lista_ordenada)  # Obtém o tamanho da lista

# Verifica se o número de elementos é par ou ímpar para calcular a mediana
if tamanho % 2 == 0:
    # Se o número de elementos é par, a mediana é a média dos dois valores centrais
    indice1 = tamanho // 2 - 1
    indice2 = tamanho // 2
    mediana = (lista_ordenada[indice1] + lista_ordenada[indice2]) / 2
else:
    # Se o número de elementos é ímpar, a mediana é o valor central
    indice = tamanho // 2
    mediana = lista_ordenada[indice]

# Imprime a mediana dos elementos na lista
print("A mediana dos elementos na lista é:", mediana)

# Calcula a média
# Soma todos os valores na lista
soma = sum(lista_numeros)
# Calcula a média dividindo a soma pelo número de elementos
media = soma / len(lista_numeros)

# Imprime a média dos elementos na lista
print("A média dos elementos na lista é:", media)