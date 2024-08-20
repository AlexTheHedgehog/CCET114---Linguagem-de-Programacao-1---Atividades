while True:
    try:
        n = int(input())
        diag = n-1
        matriz = []

        for i in range(n):
            linha = []
            for j in range(n):
                if j == diag:
                    linha.append(2)
                    diag -= 1
                else:
                    if i == j:
                        linha.append(1)
                    else:
                        linha.append(3)
                
            matriz.append(linha)


        for i in range(n):
            for j in range(n):
                print(matriz[i][j], end='')
        
            print()

    except EOFError:
        break