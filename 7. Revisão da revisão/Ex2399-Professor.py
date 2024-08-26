n = int(input())
campo = []
for i in range(n):
    mina = int(input())
    campo.append(mina)

res = [0]*n

for i in range(n):
    res[i] += campo[i]
    if i < n-1:
        res[i] += campo[i+1]
    elif i > 0:
        res[i] += campo[i-1]

for i in range(n):
    print(res[i])