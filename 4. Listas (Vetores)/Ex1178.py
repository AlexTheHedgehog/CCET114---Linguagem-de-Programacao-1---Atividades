x = float(input())
n = [x]

for i in range (1, 100):
    x /= 2
    n.append(x)

for i in range(0, 100):
    print(f'N[{i}] = {n[i]:.4f}')