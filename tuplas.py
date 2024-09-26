a, b = input().split()

tupla2 = tuple(map(int, b.replace('(', '').replace(')', '').split(',')))
tupla1 = tuple(map(int, a.replace('(', '').replace(')', '').split(',')))

lista = []

if tupla1 > tupla2:
    for i in range(len(tupla2)):
        lista.append(tupla1[i])
        lista.append(tupla2[i])

    for i in tupla1[len(tupla2):]:
        lista.append(i)
else:
    for i in range(len(tupla1)):
        lista.append(tupla1[i])
        lista.append(tupla2[i])

    for i in tupla2[len(tupla1):]:
        lista.append(i)

'''for i in tupla1:
    lista.append(i)

for i in tupla2:
    lista.append(i)'''

tupla3 = tuple(lista)

print(tupla3)