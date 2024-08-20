n = int(input())

for i in range(n):
    qt, s = input().split()
    qt = int(qt); s = int(s)
    linha = input().split()

    for j in range(qt):
        linha[j] = int(linha[j])

    sorteado = 0
    prox = abs(s - linha[0])
    
    for j in range(1, qt):
        if abs(s - linha[j]) < prox:
            prox = abs(s - linha[j])
            sorteado = j

    print(sorteado + 1)