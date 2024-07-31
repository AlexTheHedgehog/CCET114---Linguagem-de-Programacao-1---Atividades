h1, m1, h2, m2 = map(int, input().split())
totalh = totalm = 0

if h1 < h2:
    totalh = h2 - h1
elif h1 >= h2:
    totalh = 24 - (h1 - h2)
elif h2 == (h1+1):
    totalh = 0

if m1 < m2:
    totalm = m2 - m1
elif m1 > m2:
    totalm = m1 - m2
elif m1 == m2:
    totalm = 0

print(f'O JOGO DUROU {totalh} HORA(S) E {totalm} MINUTO(S)')