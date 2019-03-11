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

qntd_pontos = 3 #int(input("Digite a quantida de pontos: "))
vetor_x = [-1.0,0.0,3.0] #list(map(float,input("Digite os valores de x: ").split()))
valores_y = [15.0,8.0,-1.0] #list(map(float,input("Digite os valores de y: ").split()))
matriz = gera_matriz(qntd_pontos,valores_y)
x = 2.0 #float(input("Informe os valores a serem interpolados"))

for i in range(2,qntd_pontos):
    for j in range(i,qntd_pontos):
        matriz[i][j] = ((matriz[i][j-1] - matriz[i-1][j-1]) / (vetor_x[j]-vetor_x[i-j+1]))
        
aprx = matriz[0][0]
mul = 1.0
print(matriz)

for t in range(1,qntd_pontos):
    if t==1:
        mul = ((matriz[t][t-1] - matriz[t-1][t-1]) / (vetor_x[t]-vetor_x[t-1]))
        for y in range(t):
            mul = mul *(x - vetor_x[0])
    else:
        mul = ((matriz[t][y] - matriz[t-1][t-1]) / (vetor_x[t]-vetor_x[y]))
        for i in range(1):
            mul = mul * (x - vetor_x[0]) * (x - vetor_x[t-1])
    aprx += mul

print( "O valor aproximado de f(%f) é: %f" %(x,aprx))