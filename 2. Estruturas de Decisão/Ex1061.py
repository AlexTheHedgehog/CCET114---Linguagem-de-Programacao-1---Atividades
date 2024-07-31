dia1 = int(input('Dia '))
h1, m1, s1 = map(int, input().replace(':', '').split())
dia2 = int(input('Dia '))
h2, m2, s2 = map(int, input().replace(':', '').split())

dias = dia2 - dia1
horas = minutos = segundos = 0

if h2 > h1:
    horas = h2 - h1
else:
    horas = 24 - (h1 - h2)

if m2 > m1:
    minutos = m2 - m1
else:
    minutos = 60 - (m1 - m2)

if s2 > s1:
    segundos = s2 - s1
else:
    segundos = 60 - (s1 - s2)

print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')