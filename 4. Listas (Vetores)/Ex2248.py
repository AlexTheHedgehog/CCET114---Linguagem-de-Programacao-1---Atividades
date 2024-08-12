"""c_maior = m_maior = 0
turma = 1
resp = ''
while True:
    n = int(input())
    if n == 0:
        break
    c = []
    m = []
    for i in range(0, n):
        x, y = map(int, input().split())
        c.append(x)
        m.append(y)

    m_maior = max(m)
    for i in range(0, n):
        if m[i] == m_maior:
            c_maior = c[i]
        
    if turma > 1:
        resp += '\n'
    resp += f'Turma {n+1}\n{c_maior}'
        

    turma += 1

print(resp)"""

turma = 1
while True:
    n = int(input())
    if n == 0:
        break

    c = []
    while n:
        n -= 1
        c.append([int(x) for x in input().split()])

    maior = max([x[1] for x in c])
    estagio = [str(x[0]) for x in c if x[1] == maior]

    print('Turma %d' % turma)
    print(' '.join(estagio), '')
    print()
    turma += 1