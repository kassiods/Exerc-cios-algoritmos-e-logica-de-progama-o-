'''Escreva um programa que leia o índice pluviométrico de cada dia do mês de
junho e informe o dia que mais choveu, o dia que menos choveu e as médias
pluviométricas de cada uma das duas quinzenas.'''

# Define o número de dias em junho
dias = 30

# Lista para armazenar os índices pluviométricos de cada dia
pluvio = [0] * dias  # Inicializa uma lista com 30 elementos (0)

# Loop para ler os índices pluviométricos de cada dia
for i in range(dias):
    pluvio[i] = float(input(f"Digite a pluviosidade do dia {i + 1} de junho: "))

# Inicializa variáveis para o dia que mais choveu e o dia que menos choveu
max_pluvio = pluvio[0]  # Assume que o primeiro valor é o máximo inicial
min_pluvio = pluvio[0]  # Assume que o primeiro valor é o mínimo inicial
dia_mais_chuvoso = 1   # Inicializa o dia mais chuvoso com o primeiro dia
dia_menos_chuvoso = 1  # Inicializa o dia menos chuvoso com o primeiro dia

# Loop para encontrar o dia que mais choveu e o dia que menos choveu
for i in range(1, dias):
    if pluvio[i] > max_pluvio:
        max_pluvio = pluvio[i]  # Atualiza o máximo pluviosidade encontrado
        dia_mais_chuvoso = i + 1  # Atualiza o dia mais chuvoso

    if pluvio[i] < min_pluvio:
        min_pluvio = pluvio[i]  # Atualiza o mínimo pluviosidade encontrado
        dia_menos_chuvoso = i + 1  # Atualiza o dia menos chuvoso

# Inicializa variáveis para as somas das quinzenas
soma_primeira_quinzena = 0
soma_segunda_quinzena = 0

# Calcula a soma da primeira quinzena
for i in range(15):
    soma_primeira_quinzena += pluvio[i]

# Calcula a soma da segunda quinzena
for i in range(15, dias):
    soma_segunda_quinzena += pluvio[i]

# Calcula as médias pluviométricas
media_primeira_quinzena = soma_primeira_quinzena / 15
media_segunda_quinzena = soma_segunda_quinzena / 15

# Exibe os resultados
print(f"O dia que mais choveu foi o dia {dia_mais_chuvoso} com {max_pluvio}mm")
print(f"O dia que menos choveu foi o dia {dia_menos_chuvoso} com {min_pluvio}mm")
print(f"Média pluviométrica da primeira quinzena: {media_primeira_quinzena:.2f}mm")
print(f"Média pluviométrica da segunda quinzena: {media_segunda_quinzena:.2f}mm")