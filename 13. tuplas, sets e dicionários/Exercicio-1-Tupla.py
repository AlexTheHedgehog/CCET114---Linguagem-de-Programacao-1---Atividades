# 1) Escreva programa que recebe como entrada
# duas tuplas de n elementos cada, em uma
# mesma linha e retorna uma tupla cujo o
# conteúdo intercala os elementos das duas
# tuplas. As tuplas de entrada podem ser de
# tamanhos diferentes.

a, b = input().split()

tupla1 = tuple(map(int, a.replace('(', '').replace(')', '').split(',')))
tupla2 = tuple(map(int, b.replace('(', '').replace(')', '').split(',')))

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

tupla3 = tuple(lista)

print(tupla3)