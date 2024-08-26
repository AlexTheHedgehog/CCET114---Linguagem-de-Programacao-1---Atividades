n = int(input())
soma_copo = 0

for i in range(n):
    lata, copo = map(int, input().split())
    if lata > copo:
        soma_copo += copo

print(soma_copo)