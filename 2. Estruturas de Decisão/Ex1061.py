dia_inicio = input().split()
dia1 = int(dia_inicio[1])
h1, m1, s1 = map(int, input().split(' : '))
dia_fim = input().split()
dia2 = int(dia_fim[1])
h2, m2, s2 = map(int, input().split(' : '))

inicio = (dia1 * 86400 + h1 * 3600 + m1 * 60 + s1)
fim = (dia2 * 86400 + h2 * 3600 + m2 * 60 + s2)
diff = fim - inicio

dias = diff // 86400
diff = diff % 86400
horas = diff // 3600
diff = diff % 3600
minutos = diff // 60
segundos = diff % 60

print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')