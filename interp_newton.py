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

qntd_pontos = 3 #int(input("Digite a quantida de pontos: "))
vetor_x = [-1.0,0.0,3.0] #list(map(float,input("Digite os valores de x: ").split()))
valores_y = [15.0,8.0,-1.0] #list(map(float,input("Digite os valores de y: ").split()))
matriz = gera_matriz(qntd_pontos,valores_y)
x = 2.0 #float(input("Informe os valores a serem interpolados"))
fs = calcula_f(qntd_pontos,vetor_x,matriz)
