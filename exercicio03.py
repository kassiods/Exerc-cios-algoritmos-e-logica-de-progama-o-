'''
Escreva um progama que calcule o imposto de renda a parTr de um salário de
um funcionário a parTr de da tabela abaixo:
Sálario IPRF
Ate 1.500,00 5%
Acima de 1500,00 até 3.000,00 8%
Acima de 3.000,00 até 10.000,00 15%
Acima de 15.000,00 27%
O programa deverá ao fim imprimir o valor deo imposto devido, o saláriio bruto
e o salário com desconto. O programa ainda deverá se repeTr até que o
usuário deseje encerra-lo.'''

# Solicita ao usuário para digitar o salário do funcionário
salario = int(input("Digite o salário do funcionário: "))

# Inicia um loop que continua enquanto o salário for maior que 0
while salario > 0:
    # Calcula o imposto com base na faixa salarial
    if salario <= 1500:
        imposto = salario * 0.05  # 5% de imposto para salários até 1500
    elif salario <= 3000:
        imposto = salario * 0.08  # 8% de imposto para salários entre 1501 e 3000
    elif salario <= 10000:
        imposto = salario * 0.15  # 15% de imposto para salários entre 3001 e 10000
    else:
        imposto = salario * 0.27  # 27% de imposto para salários acima de 10000
    
    # Imprime o salário bruto
    print(f"Salário bruto: {salario}")
    # Imprime o valor do imposto devido
    print(f"Imposto devido: {imposto}")
    # Imprime o salário após a dedução do imposto
    print(f"Salário com desconto: {salario - imposto}")
    
    # Solicita ao usuário para digitar um novo salário
    salario = int(input("Digite o salário do funcionário: "))

# O loop termina quando o salário digitado é 0 ou negativo