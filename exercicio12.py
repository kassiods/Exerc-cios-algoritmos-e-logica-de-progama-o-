#insira o credito do cliente
saldo_medio = float(input("Digite o saldo médio do cliente: "))

# Verifica o intervalo em que o saldo médio se encaixa e calcula o valor do crédito correspondente
if saldo_medio <= 200:
    # Se o saldo médio é menor ou igual a 200, o crédito é 0
    credito = 0
elif saldo_medio <= 400:
    # Se o saldo médio é maior que 200 e menor ou igual a 400, o crédito é 20% do saldo médio
    credito = saldo_medio * 0.2
elif saldo_medio <= 600:
    # Se o saldo médio é maior que 400 e menor ou igual a 600, o crédito é 30% do saldo médio
    credito = saldo_medio * 0.3
else:
    # Se o saldo médio é maior que 600, o crédito é 40% do saldo médio
    credito = saldo_medio * 0.4

# Imprime o saldo médio do cliente
print("Saldo médio: R$", saldo_medio)

# Imprime o valor do crédito calculado com base no saldo médio
print("Valor do crédito: R$", credito)