matriz = []

c = int(input())
op = input().upper()
soma = 0

#criar matriz
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    
    matriz.append(linha)

for i in range(12):
    for j in range(12):
        if j == c:
            soma += matriz[i][j]

media = soma / 12

if op == 'S':
    print(f'{soma:.1f}')
elif op == 'M':
    print(f'{media:.1f}')