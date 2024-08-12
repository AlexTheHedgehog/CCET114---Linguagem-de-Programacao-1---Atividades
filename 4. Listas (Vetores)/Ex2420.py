"""n = int(input())
a = list(map(int, input().split()))
a_soma = b_soma = 0

for i in range(0, n):
    a_soma += a[i]
    for j in range(i+1, n):
        b_soma += a[j]

    if a_soma == b_soma:
        k = i+1
        break
    
    b_soma = 0

print(k)"""
n = int(input())
a = list(map(int, input().split()))
a_soma = b_soma = 0

for i in range(n):
    a_soma+=a[i]
a_soma=a_soma/2
for i in range(n):
    b_soma+=a[i]
    if b_soma == a_soma:
        k=i+1
        print(k)
        break