n, c = map(int, input().split())
soma = 0
excedeu = 'N'

for i in range(n):
    s, e = map(int, input().split())
    soma += e - s
    if soma > c:
        excedeu = 'S'

print(excedeu)