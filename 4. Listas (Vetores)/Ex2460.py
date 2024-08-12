n = int(input())
fila = list(map(int, input().split()))
m = int(input())
sairam = list(map(int, input().split()))
resp = ''

for i in sairam:
    fila.remove(i)

for i in fila:
    resp += f'{i} '

print(resp[:len(resp)-1])