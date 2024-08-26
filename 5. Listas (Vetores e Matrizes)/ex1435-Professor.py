while True:
    n = int(input())
    if n == 0:
        break

    matriz = []

    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(cont)
            acima = i
            esqu = j
            abaixo = n-i-1
            dire = n-j-1
            d = acima

            if abaixo < d:
                d = abaixo
            if esqu < d:
                d = esqu
            if dire < d:
                d = dire
            
            linha.append(d + 1)
        matriz.append(linha)
    
    for i in range(n):
        resp = ''
        for j in range(n):
            resp += " %3d" %matriz[i][j]
        print(resp[1:])
    print()