n = int(input())
campo = []
for i in range(n):
    mina = int(input())
    campo.append(mina)

ant = 0

for i in range(n):
    if i < n-1:
        prox = campo[i+1]
    else:
        prox = 0
    cont = campo[i] + prox + ant
    print(cont)
    ant = campo[i]