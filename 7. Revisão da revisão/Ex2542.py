while True:
    try:
        n = int(input())
        m, l = map(int, input().split())
        marcos = []; leo = []

        for i in range(m):
            marcos.append(list(map(int, input().split())))

        for i in range(l):
            leo.append(list(map(int, input().split())))

        cm, cl = map(int, input().split())
        a = int(input())

        sorteados = [marcos[cm-1][a-1], leo[cl-1][a-1]]

        if sorteados[0] > sorteados[1]:
            print('Marcos')
        elif sorteados[0] < sorteados[1]:
            print('Leonardo')
        else:
            print('Empate')
    except EOFError:
        break