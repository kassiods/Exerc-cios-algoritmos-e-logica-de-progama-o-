'''
faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa,
leia o seu peso e sua altura e imprima na tela sua condição de acordo com a
tabela abaixo:
Fórmula do IMC = peso / (altura) ²
Tabela Condições IMC
Abaixo de 18,5 | Abaixo do peso
Entre 18,6 e 24,9 | Peso ideal (parabéns)
Entre 25,0 e 29,9 | Levemente acima do peso
Entre 30,0 e 34,9 | Obesidade grau I
Entre 35,0 e 39,9 | Obesidade grau II (severa)
Maior ou igual a 40 | Obesidade grau III (mórbida)
'''

# Solicita ao usuário que insira o seu peso em quilogramas
peso = float(input("Digite o seu peso: "))

# Solicita ao usuário que insira a sua altura em metros
altura = float(input("Digite a sua altura: "))

# Calcula o Índice de Massa Corporal (IMC) usando a fórmula:
# IMC = peso / (altura ** 2)
# Onde 'altura ** 2' é a altura ao quadrado
imc = peso / altura ** 2

# Avalia o valor do IMC e classifica o estado de acordo com as faixas de IMC estabelecidas
if imc < 18.5:
    # Se o IMC for menor que 18.5, imprime "Abaixo do peso"
    print("Abaixo do peso")
elif 18.6 <= imc <= 24.9:
    # Se o IMC estiver entre 18.6 e 24.9 (inclusive), imprime "Peso ideal (parabéns)"
    print("Peso ideal (parabéns)")
elif 25 <= imc <= 29.9:
    # Se o IMC estiver entre 25 e 29.9 (inclusive), imprime "Levemente acima do peso"
    print("Levemente acima do peso")
elif 30 <= imc <= 34.9:
    # Se o IMC estiver entre 30 e 34.9 (inclusive), imprime "Obesidade grau I"
    print("Obesidade grau I")
elif 35 <= imc <= 39.9:
    # Se o IMC estiver entre 35 e 39.9 (inclusive), imprime "Obesidade grau II (severa)"
    print("Obesidade grau II (severa)")
else:
    # Se o IMC for 40 ou mais, imprime "Obesidade grau III (mórbida)"
    print("Obesidade grau III (mórbida)")