'''
Construa um algoritmo que, tendo como dados de entrada dois pontos
quaisquer no plano, P(x1,y1) e P(x2,y2), escreva a distância entre eles.
A fórmula que efetua tal cálculo é: 
'''
# Solicita ao usuário a coordenada x do ponto P1 e a converte para um número de ponto flutuante (float)
x1 = float(input("Digite a coordenada x1 do ponto P1: "))

# Solicita ao usuário a coordenada y do ponto P1 e a converte para um número de ponto flutuante (float)
y1 = float(input("Digite a coordenada y1 do ponto P1: "))

# Solicita ao usuário a coordenada x do ponto P2 e a converte para um número de ponto flutuante (float)
x2 = float(input("Digite a coordenada x2 do ponto P2: "))

# Solicita ao usuário a coordenada y do ponto P2 e a converte para um número de ponto flutuante (float)
y2 = float(input("Digite a coordenada y2 do ponto P2: "))

# Calcula a distância entre os pontos P1 (x1, y1) e P2 (x2, y2) usando a fórmula da distância euclidiana
# Fórmula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
# Onde sqrt é a raiz quadrada e (x2 - x1)^2 + (y2 - y1)^2 é a soma dos quadrados das diferenças das coordenadas
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Exibe a distância calculada entre os pontos P1 e P2
print("A distância entre os pontos P1 e P2 é:", distancia)