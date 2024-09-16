t = int(input())
for i in range(t):
    garrafas = 0
    n, k = map(int, input().split())
    garrafas += (n // k) + (n % k)
    print(garrafas)