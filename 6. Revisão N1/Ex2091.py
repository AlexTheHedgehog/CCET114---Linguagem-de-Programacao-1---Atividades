while True:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))
    b = []
    for i in a:
        if i in b:
            b.remove(i)
        else:
            b.append(i)

    print(b[0])