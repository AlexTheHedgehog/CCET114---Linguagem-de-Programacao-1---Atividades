n = int(input())
r = list(map(int, input().split()))
queda = ant = 0

for i in range(0, n):
    if r[i] < ant:
        queda = i + 1
        break
    
    ant = r[i]

print(queda)