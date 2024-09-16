n, m = map(int, input().split())
campo = []
for i in range(n):
    campo.append(list(map(int, input().split())))

maior = 0
# linhas
for i in range(n):
    quant = sum(campo[i])
    if quant > maior:
        maior = quant

# colunas
for i in range(m):
    quant = 0
    for j in range(n):
        quant += campo[j][i]

    if quant > maior:
        maior = quant

print(maior)