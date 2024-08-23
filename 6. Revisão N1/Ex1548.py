n = int(input())

for i in range(n):
    cont = 0
    m = int(input())
    p1 = list(map(int, input().split()))
    p2 = p1.copy()
    p2.sort(reverse=True)

    for j in range(m):
        if p1[j] == p2[j]:
            cont += 1

    print(cont)
