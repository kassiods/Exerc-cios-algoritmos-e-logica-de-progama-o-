'''Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3%
ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de
2% ao ano, escreva um programa, que imprima o tempo necessário para que a
população do país A ultrapasse a população do país B.'''
# Define a população inicial dos dois países
pais_a = 5000000  # População inicial do país A
pais_b = 7000000  # População inicial do país B

# Inicializa o contador de anos
ano = 0  # Contador de anos necessário para a população do país A ultrapassar a do país B

# Loop para calcular a evolução da população dos dois países até que a população do país A seja maior que a do país B
while pais_a < pais_b:
    # Atualiza a população do país A com um crescimento de 3% ao ano
    pais_a *= 1.03
    
    # Atualiza a população do país B com um crescimento de 2% ao ano
    pais_b *= 1.02
    
    # Incrementa o contador de anos
    ano += 1

# Imprime o número de anos necessários para que a população do país A ultrapasse a do país B
print(f"Serão necessários {ano} anos para que a população do país A ultrapasse a população do país B")