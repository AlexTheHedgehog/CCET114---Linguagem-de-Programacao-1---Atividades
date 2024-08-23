n = int(input())
matriz = []
colet = []

for i in range(n):
    matriz.append(list(map(int, input().split())))

for i in range(n*2):
    x, y = input().split()
    x = int(x) - 1; y= int(y) - 1
    if matriz[x][y] not in colet:
        colet.append(matriz[x][y])

print(len(colet))