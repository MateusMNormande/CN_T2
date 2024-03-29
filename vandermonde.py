import numpy as np
from numpy.linalg import inv

def matriz_vm(tamanho,valores_x):
    '''
    Calcula a Matriz de Vandermonde
    '''
    matriz = []
    for i in range(len(valores_x)):
        linha = []
        for j in range(tamanho):
            valor = (valores_x[i])**j
            linha.append(valor)
        matriz.append(linha)
    return matriz

def gera_polinomio(coeficientes):
    '''
    Gera a string do polinomio
    '''
    polinomio = "%f + "%coeficientes[0]
    for i in range(1,len(coeficientes)):
        if i == len(coeficientes)-1:
            polinomio += "%fx^%i"%(coeficientes[i],i)
        else:
            polinomio += "%fx^%i + "%(coeficientes[i],i)
    return polinomio

def interpolacao(coeficientes, x):
    '''
    Calcula o valor a ser interpolado no polinomio
    '''
    p_x = 0
    for i in range(len(coeficientes)):
        p_x += coeficientes[i] * (x**i)
    return p_x
    

qntd_pontos = int(input("Digite a quantida de pontos: "))
valores_x = list(map(float,input("Digite os valores de x: ").split()))
valores_y = list(map(float,input("Digite os valores de y: ").split()))
A = matriz_vm(qntd_pontos,valores_x)
A_inv = inv(np.array(A))
b = np.array(valores_y)
coeficientes = list(np.dot(A_inv,b))
polinomio = gera_polinomio(coeficientes)
print("p(x) = %s"%polinomio)
x = float(input("Digite o valor a ser interpolado: "))
p = interpolacao(coeficientes,x)
print("p(%f) = %f"%(x,p))