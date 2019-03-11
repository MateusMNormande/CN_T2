import numpy as np

def gera_matriz(qntd_pontos,valores_y):
    matriz = []
    for i in range(qntd_pontos):
        linha = []
        for j in range(qntd_pontos):
            if j == 0:
                linha.append(valores_y[i])
            else:
                linha.append(0.0)
        matriz.append(linha)
    return matriz

def calcula_f(qntd_pontos,vetor_x,matriz):
    for i in range(1,qntd_pontos): 
        for j in range(i,qntd_pontos):
            matriz[j][i] = ( (matriz[j][i-1]-matriz[j-1][i-1]) / (vetor_x[j]-vetor_x[j-i]))
    diagonal = list(np.diagonal(matriz))
    return diagonal

def calcula_polinomio(qntd_pontos,fs,vetor_x,x):
    grau = qntd_pontos - 1
    p = fs[grau]
    for k in range(1,qntd_pontos):
        p = fs[grau-k] + (x -vetor_x[grau-k])*p
    return p
    

qntd_pontos = int(input("Digite a quantida de pontos: "))
vetor_x = list(map(float,input("Digite os valores de x: ").split()))
valores_y = list(map(float,input("Digite os valores de y: ").split()))
matriz = gera_matriz(qntd_pontos,valores_y)
x = float(input("Informe o valor a ser interpolado: "))
fs = calcula_f(qntd_pontos,vetor_x,matriz)
p = calcula_polinomio(qntd_pontos,fs,vetor_x,x)
print("p(%f) = %f"%(x,p))