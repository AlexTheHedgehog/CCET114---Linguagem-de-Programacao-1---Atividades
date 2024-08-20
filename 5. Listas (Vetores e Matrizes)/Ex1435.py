while True:
    n = int(input())
    if n == 0:
        break

    matriz = []

    for i in range(n):
        linha = []
        cont1 = i+1
        cont2 = 1
        cont = cont1
        for j in range(n):
            linha.append(cont)
            if cont1 > 1:
                cont1 -= 1
                cont = cont1
            else:
                cont2 += 1
                cont = cont2
        matriz.append(linha)
    
    for i in range(n):
        resp = ''
        for j in range(n):
            resp += " %3d" %matriz[i][j]
        print(resp[1:])
    print()