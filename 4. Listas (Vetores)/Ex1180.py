n = int(input())
a = list(map(int, input().split()))
x = []
for i in range(0, n):
    x.append(a[i])

menor = min(x)

for i in range(0, n):
    if x[i] == menor:
        posicao = i
    
print(f'Menor valor: {menor}\nPosicao: {posicao}')