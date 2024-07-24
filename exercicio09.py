'''
Escreva um programa que recebe um CPF e verifica se ele é válido ou inválido
'''

# Pergunta o CPF ao usuário
cpf = input("Digite o CPF (somente números): ")

# Verifica se o CPF tem 11 dígitos e se é composto apenas por números
if len(cpf) != 11 or not cpf.isdigit():
    # Se o CPF não tiver exatamente 11 dígitos ou não for composto apenas por números, exibe uma mensagem de erro
    print("CPF inválido.")
else:
    # Converte o CPF em uma lista de inteiros
    cpf = [int(digit) for digit in cpf]

    # Inicializa a variável para verificar se todos os caracteres são dígitos válidos
    is_valid = True
    for digit in cpf:
        if digit < 0 or digit > 9:
            # Se algum dígito não estiver no intervalo de 0 a 9, marca como inválido
            is_valid = False
            break

    if is_valid:
        # Calcula o primeiro dígito verificador do CPF
        soma1 = 0
        for i in range(9):
            # Soma os produtos dos 9 primeiros dígitos do CPF com os pesos de 10 a 2
            soma1 += cpf[i] * (10 - i)
        # Calcula o primeiro dígito verificador usando a fórmula padrão: (soma1 * 10) % 11
        # Se o resultado for maior que 9, o dígito verificador é ajustado para ser entre 0 e 9
        digito1 = (soma1 * 10 % 11) % 10

        # Calcula o segundo dígito verificador do CPF
        soma2 = 0
        for i in range(10):
            # Soma os produtos dos 10 primeiros dígitos do CPF com os pesos de 11 a 2
            soma2 += cpf[i] * (11 - i)
        # Calcula o segundo dígito verificador
        digito2 = (soma2 * 10 % 11) % 10

        # Verifica se os dígitos verificadores calculados são iguais aos fornecidos pelo usuário
        if digito1 == cpf[9] and digito2 == cpf[10]:
            # Se os dígitos verificadores coincidirem, o CPF é considerado válido
            print("CPF válido.")
        else:
            # Caso contrário, o CPF é considerado inválido
            print("CPF inválido.")
    else:
        # Se algum dígito não for válido, o CPF é considerado inválido
        print("CPF inválido.")
