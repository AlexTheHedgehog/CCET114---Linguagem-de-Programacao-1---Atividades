ordem = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
placar = [0]*4
n = int(input())

for i in range(n):
    resp = list(input().split())
    a = []; b = []

    for j in range(6):
        if j <= 2:
            a.append(int(resp[j]))
        else:
            b.append(int(resp[j]))

    for j in range(3):
        if ordem.index(a[j]) > ordem.index(b[j]) or ordem.index(a[j]) == ordem.index(b[j]):
            placar[0] += 1
        else:
            placar[1] += 1
    
    if placar[0] > placar[1]:
        placar[2] += 1
    else:
        placar[3] += 1
    
    placar[0] = 0; placar[1] = 0

print(placar[2], placar[3])