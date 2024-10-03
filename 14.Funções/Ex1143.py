n = int(input())

quad = list(map(lambda x: x**2, range(1, n+1)))
cub = list(map(lambda x: x**3, range(1, n+1)))

for i in range(n):
    print(f'{i+1} {quad[i]} {cub[i]}')