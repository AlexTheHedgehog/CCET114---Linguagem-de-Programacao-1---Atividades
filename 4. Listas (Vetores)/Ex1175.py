n = []

for i in range(0, 20):
    num = int(input())

    n.append(num)

n.reverse()

for i in range(0, 20):
    print(f'N[{i}] = {n[i]}')