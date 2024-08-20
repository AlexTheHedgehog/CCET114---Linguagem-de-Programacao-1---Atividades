n, m = input().split()
n = int(n); m = int(m)
campo = []
maior = 0

for i in range(n):
    linha = list(input().split())
    
    for j in range(m):
        linha[j] = int(linha[j])
    
    campo.append(linha)

# somando as linhas
for i in range(n):
    soma_linha = sum(campo[i])
    if soma_linha > maior:
        maior = soma_linha

# somando as colunas
for j in range(m):
    soma_coluna = 0
    for i in range(n):
        soma_coluna += campo[i][j]
    if soma_coluna > maior:
        maior = soma_coluna

print(maior)