h1, h2 = map(int, input().split())
total = 0

if h1 < h2:
    total = h2 - h1
elif h1 >= h2:
    total = 24 - (h1 - h2)

print(f'O JOGO DUROU {total} HORA(S)')