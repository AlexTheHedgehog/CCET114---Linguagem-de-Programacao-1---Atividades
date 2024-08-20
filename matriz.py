matriz = [[0]*5]*5

#criar matriz
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input())

#imprimir matriz
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end=' ')
    
    print()

print(matriz)