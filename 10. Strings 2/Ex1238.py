n = int(input())

for i in range(n):
    resp = ''
    a, b = input().split()
    if len(a) > len(b):
        maior = len(a)
    else:
        maior = len(b)
    
    for j in range(maior):
        if j + 1 <= len(a):
            resp += a[j]
        if j + 1 <= len(b):
            resp += b[j]
        
    print(resp)