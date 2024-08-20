matriz = []

l = int(input())
op = input().upper()

#criar matriz
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    
    matriz.append(linha)

soma = sum(matriz[l])
media = soma / 12

if op == 'S':
    print(f'{soma:.1f}')
elif op == 'M':
    print(f'{media:.1f}')