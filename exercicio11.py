'''
Em uma cerTficação são feitos são feitos 5 exames (I, II, III, IV e V). Escreva um
programa que leia as notas destes exames e imprima a classificação do aluno,
sabendo que a média é 7.0.
Classificação: A passou em todos os exames;
B passou em I, II e IV, mas não em III ou V;
C passou em I e II, III ou IV, mas não em V.
Reprovado outras situações.
'''
# Solicita as notas dos cinco exames
nota_I = float(input("Digite a nota do exame I: "))
nota_II = float(input("Digite a nota do exame II: "))
nota_III = float(input("Digite a nota do exame III: "))
nota_IV = float(input("Digite a nota do exame IV: "))
nota_V = float(input("Digite a nota do exame V: "))

# Calcula a média das notas dos exames
media = (nota_I + nota_II + nota_III + nota_IV + nota_V) / 5

# Determina a classificação com base nas notas
if media >= 7.0:
    if nota_I >= 7.0 and nota_II >= 7.0 and nota_III >= 7.0 and nota_IV >= 7.0 and nota_V >= 7.0:
        classificacao = 'A'
    elif nota_I >= 7.0 and nota_II >= 7.0 and (nota_III < 7.0 or nota_V < 7.0):
        classificacao = 'B'
    elif (nota_I >= 7.0 and nota_II >= 7.0) and (nota_III >= 7.0 or nota_IV >= 7.0) and nota_V < 7.0:
        classificacao = 'C'
    else:
        classificacao = 'Reprovado'
else:
    classificacao = 'Reprovado'

# Imprime a classificação
print(f"A classificação do aluno é: {classificacao}")