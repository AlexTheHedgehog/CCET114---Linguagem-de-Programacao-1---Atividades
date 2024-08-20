n = -1

while n != 0:
    n = int(input())
    try:
        sus = input().split()
    except EOFError:
        break
    
    for i in range(n):
        sus[i] = int(sus[i])
    
    sor = sorted(sus)

    for i, j in enumerate(sus):
        if j == sor[n-2]:
            print(i+1)
            break